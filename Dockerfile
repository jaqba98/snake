FROM python

WORKDIR /app

copy . /app

RUN pip install keyboard

CMD ["python3", "snake.py"]

