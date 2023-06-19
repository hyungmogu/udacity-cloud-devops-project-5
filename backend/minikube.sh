#!/bin/bash
minikube start && \
kubectl apply -f ../.circleci/kubernetes/base/