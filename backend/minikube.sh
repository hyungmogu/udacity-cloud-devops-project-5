#!/bin/bash
./venv/bin/python3 ./prepare_kubernetes.py && \
minikube start && \
kubectl apply -f ../.circleci/kubernetes/base_src/