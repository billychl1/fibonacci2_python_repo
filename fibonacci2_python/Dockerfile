FROM python:3.6-slim

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip

ENV PYTHONPATH ":/app"

ENV FLASK_APP=main.py

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask" ]

CMD ["run", "--host", "0.0.0.0"]