FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

COPY ./requirements.txt /app/requirements.txt
COPY ./scripts/requirements.txt /scripts/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN pip install -r /scripts/requirements.txt

COPY ./app ./app
COPY ./scripts ./scripts
EXPOSE 8000