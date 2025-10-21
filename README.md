# 🚀 AWS Container Observability Demo

This project demonstrates how to build, deploy, and observe containerized applications on **AWS** using **ECR**, **EKS**, **Docker**, and **GitHub Actions** for CI/CD — all within AWS Free Tier limits.

---

## 🎯 Project Goals

- Automate build and deployment of containerized apps using GitHub Actions  
- Use **AWS ECR** for storing container images  
- Deploy the app on **Amazon EKS (Kubernetes)**  
- Implement monitoring and logging with **AWS-native tools** (CloudWatch, Container Insights)  
- Demonstrate modern DevOps practices with **CI/CD pipelines**

---

## 🧰 Tools & Technologies

| Tool | Purpose |
|------|----------|
| **AWS ECR** | Container image registry |
| **AWS EKS** | Kubernetes cluster |
| **Docker** | Containerize applications |
| **GitHub Actions** | CI/CD automation |
| **CloudWatch / Container Insights** | Observability and metrics |
| **kubectl / eksctl** | Cluster management |

---

## ⚙️ Architecture Overview

```text
              +---------------------------+
              |        GitHub Repo         |
              |  (Code + CI/CD Workflow)   |
              +-------------+--------------+
                            |
                    [ GitHub Actions ]
                            |
                            v
        +-------------------+-------------------+
        |   AWS ECR (Image Repository)          |
        |   Stores Docker Images                |
        +-------------------+-------------------+
                            |
                            v
        +---------------------------------------+
        |    Amazon EKS Cluster (Kubernetes)    |
        |    Deploys and manages containers     |
        +---------------------------------------+
                            |
                            v
                 +---------------------+
                 | AWS CloudWatch Logs |
                 | & Container Insights |
                 +---------------------+
