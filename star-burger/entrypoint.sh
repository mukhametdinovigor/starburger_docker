#!/bin/sh

cd /star-burger/star-burger/

npm install --also=dev
npm install -g parcel@latest
parcel build bundles-src/index.js --dist-dir bundles --public-url="./"
python manage.py collectstatic --no-input
python manage.py migrate

exec "$@"