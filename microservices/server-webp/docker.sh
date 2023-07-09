#!/bin/bash
# if .env file exists, export all variables from it
if [ -f .env ]; then
  export $(xargs < .env);
fi

# Remove docker image if it exists
if [ "$(docker images -q "$SERVER_WEBP_DOCKER_IMAGE_NAME:$SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER" 2> /dev/null)" != "" ]; then
    docker image rm "$SERVER_WEBP_DOCKER_IMAGE_NAME:$SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER";
fi

# Build docker image and push it to docker hub
docker build -t "$SERVER_WEBP_DOCKER_IMAGE_NAME:$SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER" . &&\ 
docker login -u "$DOCKER_ID" -p "$DOCKER_PASSWORD" &&\
docker tag "$SERVER_WEBP_DOCKER_IMAGE_NAME:$SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER" "$DOCKER_ID/$SERVER_WEBP_DOCKER_IMAGE_NAME:$SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER" &&\
docker push "$DOCKER_ID/$SERVER_WEBP_DOCKER_IMAGE_NAME:$SERVER_WEBP_DOCKER_IMAGE_BUILD_NUMBER";
