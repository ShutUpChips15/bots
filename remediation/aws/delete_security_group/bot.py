import logging
import sonrai.platform.aws.arn


def run(ctx):
    # Create AWS EC2 client
    ec2_client = ctx.get_client().get('ec2')

    # Parse resource id to group
    group_id = ctx.resource_id

    # Refers doc https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html?highlight=delete%20security%20group#EC2.Client.delete_security_group
    # Refers doc https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html
    response = ec2_client.delete_security_group(GroupId=group_id,)
    logging.info(response)

    # TODO
    # Double check GroupName for defaultVPC or EC2-Classic
