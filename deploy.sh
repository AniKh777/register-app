#!/bin/bash
docker build -t register-app .
docker build -t register-app-logger -f Dockerfile.logger .
kind load docker-image register-app:v1 --name ci-cluster
kind load docker-image register-app-logger:v1 --name ci-cluster
kubectl apply -f register-app-deployment.yaml
kubectl get pods
kubectl get services
