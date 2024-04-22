from .config import settings
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError ,jwt
from datetime import datetime,timedelta,UTC


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    enc = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return enc

