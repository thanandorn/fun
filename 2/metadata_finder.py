#!/usr/bin/env python3

import datetime, argparse
import boto3
import json

def datetime_reformat(time):
    if isinstance(time, datetime.datetime):
        return time.isoformat()

def list_instances():
    client = boto3.client('ec2')
    return client.describe_instances()['Reservations']

def get_instance_metadata(instance_id):
    instances = list_instances()
    instance_metadata = {}
    for i in range(len(instances)):
        if instances[i]['Instances'][0]['InstanceId'] == instance_id:
            instance_metadata = instances[i]['Instances'][0]
    return instance_metadata

def main():
    parser = argparse.ArgumentParser(prog='metadata_finder', description='Find Metadata of an EC2 Instance')
    parser.add_argument('instance_id', type=str, help='Instance ID')
    args = parser.parse_args()
    instance_metadata = get_instance_metadata(args.instance_id)
    if instance_metadata:
        print(json.dumps(instance_metadata, indent=2, sort_keys=True, default=datetime_reformat))
    else:
        print('Instance not found...')

if __name__ == '__main__':
    main()
