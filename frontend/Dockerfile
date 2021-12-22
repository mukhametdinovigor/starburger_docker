FROM node:12


WORKDIR /star-burger

RUN npm install -g parcel@latest

COPY ./star-burger/package-lock.json .
COPY ./star-burger/package.json .
RUN npm install --also=dev

COPY ./star-burger/bundles-src/ ./bundles-src/
RUN parcel build bundles-src/index.js --dist-dir bundles --public-url="./"