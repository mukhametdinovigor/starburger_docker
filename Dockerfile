# syntax=docker/dockerfile:1

FROM python:3.8.3-alpine

# set work directory
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt
#RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2
#COPY ./entrypoint.sh .
#RUN sed -i 's/\r$//g' /app/entrypoint.sh
#RUN chmod +x /app/entrypoint.sh
COPY . .

#ENTRYPOINT ["/app/entrypoint.sh"]
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:80" ]