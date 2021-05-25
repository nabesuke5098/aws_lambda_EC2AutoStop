import boto3

REGION_NAME = 'ap-northeast-1'
STATE_LIST = ['running', 'stopped']

def get_instance_list(ec2):
    instances = ec2.describe_instances(
        Filters = [
            {'Name': 'instance-state-name', 'Values': STATE_LIST},
            {'Name': 'tag:AutoStop', 'Values': ['true']}
        ]
    )['Reservations']
    
    targetList = []
    
    if len(instances) != 0:
        for i in instances:
            instanceId = i['Instances'][0]["InstanceId"]
            targetList.append(instanceId)

    print(targetList)

    return targetList


def lambda_handler(event, context):
    ec2 = boto3.client('ec2', REGION_NAME)
    
    instanceIds = get_instance_list(ec2)
    ec2.stop_instances(InstanceIds=instanceIds)
    print('stopped your instances: ' + str(instanceIds))