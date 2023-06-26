#!/bin/bash
# if .env file exists, export all variables from it
if [ -f .env ]; then
  export $(xargs < .env);
fi

if [ "$(docker images -q "$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER" 2> /dev/null)" != "" ]; then
    docker image rm "$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER";
fi

docker build -t "$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER" . &&\ 
docker login -u "$DOCKER_ID" -p "$DOCKER_PASSWORD" &&\
docker tag "$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER" "$DOCKER_ID/$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER" &&\
docker push "$DOCKER_ID/$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER";
