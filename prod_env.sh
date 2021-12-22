#!/bin/bash

git pull

docker-compose -f docker-compose.prod.yml down
docker-compose -f docker-compose.prod.yml up -d
docker-compose -f docker-compose.prod.yml exec web python star-burger/manage.py migrate
sudo cp -r /var/lib/docker/volumes/starburger_docker_bundles_volume/_data/. /var/lib/docker/volumes/starburger_docker_static_volume/_data
sudo rm -f /var/lib/docker/volumes/starburger_docker_conf/_data/default.conf
sudo cp ./nginx.conf /var/lib/docker/volumes/starburger_docker_conf/_data
docker-compose -f docker-compose.prod.yml restart nginx

echo "Deploy is done"