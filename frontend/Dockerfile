FROM node:12


WORKDIR /star-burger

RUN npm install --also=dev
RUN npm install -g parcel@latest

COPY ./star-burger/package-lock.json .
COPY ./star-burger/package.json .
COPY ./star-burger/bundles-src/ ./bundles-src/
