from dotenv import load_dotenv
import os
from .const import BASE_DIR

dotenv_path = BASE_DIR + "/.env"
load_dotenv(dotenv_path)

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")

RABBITMQ_USERNAME = os.getenv("RABBITMQ_USERNAME")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD")
RABBITMQ_HOST = os.getenv("RABBITMQ_HOST")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT")
RABBITMQ_VHOST = os.getenv("RABBITMQ_VHOST")

SQLALCHEMY_ASYNC_DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)

EXCHANGE_LOGIN = os.getenv("EXCHANGE_LOGIN")
EXCHANGE_PASSWORD = os.getenv("EXCHANGE_PASSWORD")
