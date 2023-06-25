#!/bin/bash
python ./prepare_kubernetes.py && \
minikube start && \
kubectl apply -f ../.circleci/kubernetes/base_src/