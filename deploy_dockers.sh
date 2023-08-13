#!/bin/bash
eval $(minikube docker-env)
for d in ./microservices/*/ ; do (cd $d && sh deploy.sh); done