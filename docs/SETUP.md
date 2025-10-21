# ⚙️ Setup Instructions

This document explains how to set up and deploy the **AWS Container Observability Demo** project using **ECR**, **EKS**, **Docker**, and **GitHub Actions** — all within AWS Free Tier limits.

---

## 🧰 Prerequisites

Before you start, make sure you have:

- An **AWS Account**
- **IAM user** with programmatic access (Administrator privileges)
- Installed locally:
  - [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
  - [kubectl](https://kubernetes.io/docs/tasks/tools/)
  - [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html)
  - [Docker](https://docs.docker.com/get-docker/)
  - [Git](https://git-scm.com/downloads)

---

## 🧾 1. Clone the Repository


git clone https://github.com/ManvendraSinghShekhawat/aws-container-observability-demo.git
cd aws-container-observability-demo

## 🧾 2. Create an EKS Cluster

eksctl create cluster -f infra/eks-cluster.yaml

**To verify:**
kubectl get nodes -o wide


## 🧱 3. Build and Push Docker Image to ECR

**Authenticate Docker to ECR:**
aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.eu-west-1.amazonaws.com

**Build and Tag Image:**
docker build -t observability-demo .
docker tag observability-demo:latest <aws_account_id>.dkr.ecr.eu-west-1.amazonaws.com/observability-demo:latest

**Push to ECR:**
docker push <aws_account_id>.dkr.ecr.eu-west-1.amazonaws.com/observability-demo:latest


## 🚀 4. Deploy the Application on EKS

**Apply your Kubernetes manifests:**
kubectl apply -f infra/deployment.yaml
kubectl apply -f infra/service.yaml

**Check if pods are running:**
kubectl get pods


## 🔍 5. Enable CloudWatch Observability

i.) Go to the EKS Cluster in AWS Console

ii.) Navigate to Monitoring → Enable Container Insights

iii.) Verify metrics and logs appear under CloudWatch → Container Insights


## ⚙️ 6. Configure CI/CD with GitHub Actions

**Your GitHub Actions workflow (in .github/workflows/ci-cd.yaml) automates:**

• Docker image build

• Push to ECR

• Deploy to EKS

**To trigger it:**

• Commit and push code to the main branch

• The workflow runs automatically under GitHub → Actions


## ✅ 7. Verify Deployment

kubectl get svc
kubectl get pods
kubectl get deployments

**Access your service via LoadBalancer endpoint:**

kubectl get svc <service-name> -o wide


## 🧹 8. Cleanup

When finished, delete the cluster:
eksctl delete cluster --name my-eks-cluster



