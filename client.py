import boto3

def create_client_via_assume_role(clientName, accountId, roleName):
    client = boto3.client('sts')
    creds = client.assume_role(
        RoleArn='arn:aws:iam::{0}:role/{1}'.format(accountId, roleName),
        RoleSessionName="MacieImportCLI"
    )

    return boto3.client(clientName,
                        aws_access_key_id= creds['Credentials']['AccessKeyId'],
                        aws_secret_access_key=creds['Credentials']['SecretAccessKey'],
                        aws_session_token=creds['Credentials']['SessionToken']
            )

def get_account_id():
    client = boto3.client('sts')
    return client.get_caller_identity()['Account']