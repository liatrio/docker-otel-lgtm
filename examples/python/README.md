# My Python App Deployment Guide

This guide outlines the steps to build, deploy, and test a Python application using Docker, k3d, and k6.

## Prerequisites

- Docker
- k3d
- kubectl
- Skaffold (optional)
- k6

## Steps

### 1. Build the Docker Image

```sh
docker build -t ttl.sh/my-python-app .
```

### 2. Push the Docker Image

```sh
docker push ttl.sh/my-python-app
```

### 3. Set Up the k3d Cluster

```sh
k3d cluster create -p "8081:80@loadbalancer"
```

### 4. Deploy LGTM

```sh
kubectl apply -f lgtm.yaml
```

### 5. Port Forward LGTM Service

```sh
kubectl port-forward svc/lgtm 3000:3000
```

### 6. Deploy Application Manifests

```sh
# Preferred method
skaffold dev

# Alternative method
kubectl apply -f manifests.yaml
```

### 7. Run k6 Tests

```sh
k6 run readiness.js
k6 run fibby.js
```

## TODO

- Improve the k6 tests to cover both readiness and the application with a single test.
- Explore adding Honeycomb support to the collector exporter:
  - Investigate the integration process.
  - Identify specific attributes Honeycomb expects.
