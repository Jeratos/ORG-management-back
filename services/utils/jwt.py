from fastapi import HTTPException, status
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "s8#@aa*@^%dhb@(*vj*31356bajksbdfwe"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data):
    # to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # to_encode.update({"exp": expire})
    to_encode= {
        "email": data.organization_email,
        "id": data.id,
        "super_admin_email": super_admin_email,
        "exp": expire
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt