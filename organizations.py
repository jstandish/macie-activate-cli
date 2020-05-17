import boto3
client = boto3.client('organizations')

def get_roots():
    response = client.list_roots()

    return response['Roots']

def list_ous(parentOuId):
    response = client.list_organizational_units_for_parent(
        ParentId=parentOuId,
    )

    return response['OrganizationalUnits']

def list_accounts(parentOuId):
    response = client.list_accounts_for_parent(
        ParentId=parentOuId,
    )

    return response['Accounts']