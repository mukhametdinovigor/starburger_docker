#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
#python3 manage.py collectstatic --no-input
#python manage.py flush --no-input
#python manage.py migrate
npm install --dev
npm install -g parcel@latest
parcel build bundles-src/index.js --dist-dir bundles --public-url="./"
python3 manage.py collectstatic --no-input
python3 manage.py migrate

exec "$@"