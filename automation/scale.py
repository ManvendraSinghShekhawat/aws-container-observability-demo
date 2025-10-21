
#!/usr/bin/env python3
import argparse, subprocess
parser=argparse.ArgumentParser()
parser.add_argument("--replicas",type=int,required=True)
args=parser.parse_args()
subprocess.run(["kubectl","scale","deployment/sample-app",f"--replicas={args.replicas}"], check=True)
print("Scaled to", args.replicas)
