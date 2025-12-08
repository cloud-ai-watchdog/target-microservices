# Target Microservices

This repository contains three microservices: `target-backend`, `target-frontend`, and `loadgenerator`.

## Prerequisites

- A running Kubernetes cluster
- `gcloud` CLI installed and configured
- `helm` CLI installed

## Deployment

### 1. Connect to the Kubernetes Cluster

First, you need to connect to your GKE cluster:

```bash
gcloud container clusters get-credentials cloud-ai-police-gke --region us-central1-a
```

### 2. Deploy the Backend Service

To deploy the `target-backend` service, you can use the following Helm command.

#### Dry Run

It's always a good practice to perform a dry run first to see the generated Kubernetes manifests:

```bash
helm upgrade --install target-backend-release target-backend/helm-chart --namespace default --create-namespace --dry-run
```

#### Deploy

Once you are satisfied with the dry run, you can deploy the service:

```bash
helm upgrade --install target-backend-release target-backend/helm-chart --namespace default --create-namespace
```

### 3. Deploy the Frontend Service

Similarly, to deploy the `target-frontend` service, you can use the following Helm command.

#### Dry Run

```bash
helm upgrade --install target-frontend-release target-frontend/helm-chart --namespace default --create-namespace --dry-run
```

#### Deploy

```bash
helm upgrade --install target-frontend-release target-frontend/helm-chart --namespace default --create-namespace
```

### 4. Deploy the Loadgenerator CronJob

To deploy the `loadgenerator` CronJob, you can use the following Helm command.

#### Dry Run

```bash
helm upgrade --install loadgenerator-release loadgenerator/helm-chart --namespace default --create-namespace --dry-run
```

#### Deploy

```bash
helm upgrade --install loadgenerator-release loadgenerator/helm-chart --namespace default --create-namespace
```

## Uninstallation

To uninstall a release, you can use the `helm uninstall` command. For example, to uninstall the `target-backend-release`:

```bash
helm uninstall target-backend-release --namespace default
```
