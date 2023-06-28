#!/bin/bash
python3 -m venv ./venv &&\
./venv/bin/pip install python-dotenv==1.0.0
./venv/bin/python3 ./prepare_kubernetes.py && \
minikube start && \
kubectl apply -f ../.circleci/kubernetes/base_src/
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
