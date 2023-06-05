FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask

ENV FLASK_APP=emailinator5000.py

CMD ["flask", "run", "--host=0.0.0.0"]
