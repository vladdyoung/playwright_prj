FROM python:latest

WORKDIR /app
COPY requirements.txt .

RUN ["pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["chmod", "777", "/app"]

ENV TOKEN=${TOKEN}
ENV EMAIL=${EMAIL}

ENTRYPOINT pytest tests --headed --vault_token=${TOKEN}