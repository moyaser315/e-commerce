from fastapi import FastAPI, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

from .database import engine
from .models import product as db_product
from .models import seller, user, buyer, cartItem, order, orderItem
from .routers import product, homepage, auth, cartItems, checkout
from .routers import user as routers_user

app = FastAPI()


origins = ["http://localhost", "http://localhost:8080", "http://localhost:5173", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db_product.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)
buyer.Base.metadata.create_all(bind=engine)
seller.Base.metadata.create_all(bind=engine)
cartItem.Base.metadata.create_all(bind=engine)
orderItem.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.post("/login/test")
# def login(
#     user_cerd : OAuth2PasswordRequestForm = Depends()
# ):
#     return {"access_token": user_cerd.username}
app.include_router(homepage.router)
app.include_router(product.router)
app.include_router(routers_user.router)
app.include_router(auth.router)
app.include_router(cartItems.router)
app.include_router(checkout.router)
