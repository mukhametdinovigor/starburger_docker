# syntax=docker/dockerfile:1

FROM python:3.8-slim

# set work directory
WORKDIR /star-burger
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY /star-burger/requirements.txt requirements.txt
RUN apt-get update && apt-get -y install libpq-dev gcc && apt-get -y install nodejs
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r requirements.txt
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
COPY . .

#ENTRYPOINT ["/app/entrypoint.sh"]
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:80" ]