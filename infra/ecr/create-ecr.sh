
#!/bin/bash
set -e
AWS_REGION=${AWS_REGION:-eu-west-1}
REPO=${REPO_NAME:-sample-app}

aws ecr describe-repositories --repository-names $REPO --region $AWS_REGION >/dev/null 2>&1 || \
aws ecr create-repository --repository-name $REPO --region $AWS_REGION

echo "ECR repository $REPO ready in $AWS_REGION"
