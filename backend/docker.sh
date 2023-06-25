#!/bin/bash
# if .env file exists, export all variables from it
if [ -f .env ]; then
  export $(xargs < .env);
fi

docker build -t "$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER" .;
docker login -u "$DOCKER_ID" -p "$DOCKER_PASSWORD";
docker push "$SERVER_DOCKER_IMAGE_NAME:$SERVER_DOCKER_IMAGE_BUILD_NUMBER";
