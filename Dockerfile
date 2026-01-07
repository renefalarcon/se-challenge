FROM python:3.11-slim

LABEL name="drimo-python"
LABEL version="1.0"
LABEL description="API Software Engineer Challenge"
LABEL maintainer="rene.alarcon"

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
