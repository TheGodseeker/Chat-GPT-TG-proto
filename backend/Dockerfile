FROM python:3.11

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade -r requirements.txt

COPY . /app

CMD alembic upgrade head && uvicorn src.main:app --reload --host 0.0.0.0 --port 8080
