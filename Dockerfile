FROM ubuntu

WORKDIR /app

copy . /app

RUN apt-get update
RUN apt-get install pip -y
RUN pip install readchar --break-system-packages

CMD ["python3", "snake.py"]

