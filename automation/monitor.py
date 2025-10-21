#!/usr/bin/env python3
import boto3,os,datetime
region=os.getenv("AWS_REGION","eu-west-1")
cwlogs=boto3.client("logs",region_name=region)
# adjust log group name based on aws-for-fluent-bit config
log_group=f"/aws/containerinsights/{os.getenv('CLUSTER_NAME','my-eks-cluster')}/application"
print("Fetching recent logs from", log_group)
start=int((datetime.datetime.utcnow()-datetime.timedelta(hours=1)).timestamp()*1000)
resp=cwlogs.filter_log_events(logGroupName=log_group,startTime=start,limit=50)
for e in resp.get("events",[]):
    msg=e["message"]
    if "error" in msg.lower() or "exception" in msg.lower():
        print("[FOUND]", msg)
print("Done.")

