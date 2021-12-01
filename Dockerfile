# syntax=docker/dockerfile:1

FROM python:3.8.3-alpine

WORKDIR /star-burger
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY /star-burger/requirements.txt requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev nodejs npm tiff-dev \
jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev libwebp-dev tcl-dev tk-dev harfbuzz-dev \
fribidi-dev libimagequant-dev libxcb-dev libpng-dev

RUN rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list


RUN pip3 install -r requirements.txt
RUN sed -i 's/\r$//g'/star-burger/star-burger/entrypoint.sh
RUN chmod +x /star-burger/star-burger/entrypoint.sh
COPY . .

ENTRYPOINT ["/star-burger/star-burger/entrypoint.sh"]
