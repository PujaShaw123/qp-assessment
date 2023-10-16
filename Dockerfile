FROM tiangolo/uvicorn-gunicorn:python3.9-slim

EXPOSE 8000

COPY ./requirements.txt ./*.json /app/

WORKDIR /app

USER root
RUN pip install --no-cache-dir -r ./requirements.txt
HEALTHCHECK NONE

COPY ./src /app/app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]