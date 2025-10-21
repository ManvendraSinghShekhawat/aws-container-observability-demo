#!/usr/bin/env python3
import boto3, os, subprocess, sys
AWS_REGION=os.getenv("AWS_REGION","eu-west-1")
REPO=os.getenv("REPO_NAME","sample-app")
sts=boto3.client("sts", region_name=AWS_REGION)
account=sts.get_caller_identity()["Account"]
image=f"{account}.dkr.ecr.{AWS_REGION}.amazonaws.com/{REPO}:latest"
print("Updating deployment to image:", image)
subprocess.run(["kubectl","set","image","deployment/sample-app",f"sample-app={image}"], check=True)
subprocess.run(["kubectl","rollout","status","deployment/sample-app"], check=True)
print("Done.")

