#!/bin/bash

git pull
docker-compose down
docker-compose build
docker-compose up -d

echo "Deploy is done"