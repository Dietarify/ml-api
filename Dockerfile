FROM python:3.12.0

WORKDIR /app
COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD [ "uvicorn", "--host", "0.0.0.0", "--app-dir", "src", "main:app" ]
