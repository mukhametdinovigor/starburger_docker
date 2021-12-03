FROM node:12


WORKDIR /star-burger

COPY ./star-burger/package-lock.json .
COPY ./star-burger/package.json .
COPY ./star-burger/bundles-src/ ./bundles-src/

RUN npm install --also=dev
RUN npm install -g parcel@latest
