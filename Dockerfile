FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt
EXPOSE 50051

CMD ["bash", "-c", "if [ '$RUN_CLIENT' = '1' ]; then python client/client.py; else python server/server.py; fi"]
