import secrets
from typing import Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import HTTPException, Depends
from starlette import status
from functools import wraps


from src.settings.config import EXCHANGE_LOGIN, EXCHANGE_PASSWORD


security = HTTPBasic()


def auth_check(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
) -> bool:
    current_username_bytes = (
        credentials.username.encode("utf8") if credentials else None
    )
    current_password_bytes = (
        credentials.password.encode("utf8") if credentials else None
    )

    if not current_username_bytes or not current_password_bytes:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    correct_username_bytes = EXCHANGE_LOGIN.encode("utf8")
    correct_password_bytes = EXCHANGE_PASSWORD.encode("utf8")

    if secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    ) and secrets.compare_digest(current_password_bytes, correct_password_bytes):
        return credentials.username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Basic"},
    )


def login_required(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if not kwargs["credentials"]:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return await func(*args, **kwargs)

    return wrapper
