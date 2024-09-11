FROM python:3.9-slim

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 50051

CMD ["python", "server/server.py"]