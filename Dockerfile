FROM python:3.9.16-alpine
WORKDIR /app

ENV APP_ENV=production

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
CMD gunicorn run:app