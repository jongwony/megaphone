import boto3


def get_parameter(name):
    ssm = boto3.client('ssm', region_name='ap-northeast-2')
    return str(ssm.get_parameter(Name=name)['Parameter']['Value'])
