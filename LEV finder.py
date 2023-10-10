#!/usr/bin/env python3


import argparse
import os
def find():
    envs = ["PATH", "PWD", "LS_COLORS"]
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--command", metavar="", required=True)
    args = parser.parse_args()
    command = args.command
    for env in envs:
        sys_env = os.popen(f"echo ${env}").read()
        try:
            x = sys_env.index(command)
            x = (f"{{${env}:{x}:1}}")
            print(x.replace("{$", "${"))
        except ValueError:
            pass
        
find()