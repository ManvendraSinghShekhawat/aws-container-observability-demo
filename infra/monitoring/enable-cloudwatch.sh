#!/bin/bash
set -e
AWS_REGION=${AWS_REGION:-eu-west-1}

# Install aws-for-fluent-bit (sends logs to CloudWatch Logs)
kubectl create namespace amazon-cloudwatch || true
helm repo add aws-for-fluent-bit https://aws.github.io/eks-charts
helm repo update

helm upgrade --install aws-for-fluent-bit aws-for-fluent-bit/aws-for-fluent-bit \
  --namespace amazon-cloudwatch \
  --set cloudWatch.region=$AWS_REGION \
  --set cloudWatch.logGroup=/aws/containerinsights/${CLUSTER_NAME}/application \
  --set output.elasticsearch.enabled=false \
  --set cloudWatch.createLogGroup=true \
  --wait --timeout 10m

