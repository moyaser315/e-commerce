from fastapi import FastAPI, Request
from starlette.concurrency import iterate_in_threadpool
from starlette.background import BackgroundTask
from fastapi.middleware.cors import CORSMiddleware
from logging.config import dictConfig
import logging
import time
from fastapi.staticfiles import StaticFiles
from backend.database import engine
from backend.models import product as db_product
from backend.models import seller, user, buyer, cartItem, order, orderItem
from backend.routers import product, homepage, cartItems, checkout
from backend.routers import user as routers_user
from backend.schemas.logging import LogConfig
from backend.routers import reports

# setup
## loggging
logging.basicConfig(filename="info.log", level=logging.DEBUG)
dictConfig(LogConfig().model_dump())
logger = logging.getLogger(__name__)


def log_request(request: dict[str, str], response: dict[str, str]):
    log = {"request": request, "response": response}

    logger.info(log)


## app
app = FastAPI()
origins = ["http://localhost", "http://localhost:8080", "http://localhost:5173", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/static", StaticFiles(directory="static"), name="static")
## models
db_product.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
buyer.Base.metadata.create_all(bind=engine)
seller.Base.metadata.create_all(bind=engine)
cartItem.Base.metadata.create_all(bind=engine)
orderItem.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def root(req: Request, call_next):
    # request log
    req_info = {
        "method": req.method,
        "url": req.url,
        "headers": dict(req.headers),
        "body": await req.body(),
    }

    # response log
    start_time = time.perf_counter()
    response = await call_next(req)
    end_time = time.perf_counter()

    ## get response body
    response_body = [chunk async for chunk in response.body_iterator]
    response.body_iterator = iterate_in_threadpool(iter(response_body))
    response_body = str(response_body)

    response_info = {
        "status_code": response.status_code,
        "time_taken": end_time - start_time,
        "body": response_body,
    }

    task = BackgroundTask(log_request, req_info, response_info)
    response.background = task
    return response


app.include_router(product.router)
app.include_router(routers_user.router)

app.include_router(cartItems.router)
app.include_router(checkout.router)
app.include_router(homepage.router)
app.include_router(reports.router)
