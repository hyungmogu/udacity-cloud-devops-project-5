#!/bin/bash
# if .env file exists, export all variables from it
if [ -f .env ]; then
  export $(xargs < .env);
fi

# Remove docker image if it exists
if [ "$(docker images -q "$GATEWAY_DOCKER_IMAGE_NAME:$IMAGE_BUILD_NUMBER" 2> /dev/null)" != "" ]; then
    docker image rm "$GATEWAY_DOCKER_IMAGE_NAME:$IMAGE_BUILD_NUMBER";
fi

# Build docker image and push it to docker hub
docker build -t "$GATEWAY_DOCKER_IMAGE_NAME:$IMAGE_BUILD_NUMBER" . &&\ 
docker login -u "$DOCKER_ID" -p "$DOCKER_PASSWORD" &&\
docker tag "$GATEWAY_DOCKER_IMAGE_NAME:$IMAGE_BUILD_NUMBER" "$DOCKER_ID/$GATEWAY_DOCKER_IMAGE_NAME:$IMAGE_BUILD_NUMBER" &&\
docker push "$DOCKER_ID/$GATEWAY_DOCKER_IMAGE_NAME:$IMAGE_BUILD_NUMBER";
