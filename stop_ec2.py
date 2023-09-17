import boto3
from slack import WebClient
from keys import SLACK_BOT_TOKEN

# Load the Slack Client
client = WebClient(token=SLACK_BOT_TOKEN)


def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Identify instances with Dev Tags and are running
    instances = ec2.describe_instances(Filters=[
        {'Name': 'tag:Environment', 'Values': ['Development']},
        {'Name': 'instance-state-name', 'Values': ['running']}])

    # For every instance grab ID and stop the instance, then send message on Slack.
    for EC2 in instances['Reservations']:
        for instance in EC2['Instances']:
            instance_id = instance['InstanceId']
            ec2.stop_instances(InstanceIds=[instance_id])
            client.chat_postMessage(channel='#test', text=f"{instance_id} has automatically been stopped")
