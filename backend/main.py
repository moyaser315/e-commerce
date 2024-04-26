from fastapi import FastAPI , Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
# from .database import engine
# from .models import person ,buyer ,specializedUser ,user
# from .routers import user as u,auth
app =FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# person.Base.metadata.create_all(bind=engine)
# user.Base.metadata.create_all(bind=engine)
# buyer.Base.metadata.create_all(bind=engine)
# specializedUser.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/login/test")
def login(
    user_cerd : OAuth2PasswordRequestForm = Depends()
):
    return {"access_token": user_cerd.username}
# # app.include_router(u.router)
# app.include_router(auth.router)

