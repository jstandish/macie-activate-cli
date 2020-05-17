from helper import confirmation, select, ask, print_headline, print_warning, print_info, print_padding
from organizations import get_roots, list_ous, list_accounts
from client import get_account_id
import sys
import boto3

def main():
    toolAckMessage = "Amazon Macie is not a free service. By using this tool you acknowledge you are responsible for all charges and actions!"
    print_headline("Amazon Macie Activation Process Tool")
    print("!!!!!!!!!!")
    print_warning(toolAckMessage)
    print_info("See Amazon Macie pricing: https://aws.amazon.com/macie/pricing/")
    print("!!!!!!!!!!")
    cont = confirmation("Do you wish to continue?")

    if not cont:
        sys.exit(0)

    print_padding(len(toolAckMessage), '-')

    selectedOrg = select( "Select organization root:", get_roots(), lambda x : x['Name'] )
    selectedOu = select( "Select Child OU:", list_ous(selectedOrg['Id']), lambda x: x['Name'] )

    allAccounts = confirmation("Do you want to use all accounts in the OU?")
    accounts = list_accounts(selectedOu['Id'])
    selectedAccounts = accounts

    if allAccounts == False:
        selectedAccounts = [select( "Select Target Account:", accounts, lambda x: x['Name'] )]

    rawTags = ask("What tags should be added to the Macie enrolled accounts? (Format: key:value;key:value)")

    tags = {}

    for t in rawTags.split(';'):
        spl = t.split(':')
        tags[spl[0]] = spl[1]

    listOfAccountConfirm = '\n'.join(sorted(entry['Id'] for entry in selectedAccounts))
    agree = confirmation('Accounts:\n{2}\nDo you wish to enable Macie in {0} account{1}?'.format(len(selectedAccounts), 's' if len(selectedAccounts) == 0 else '', listOfAccountConfirm ))

    if agree == False:
        sys.exit(0)

    # Create Macie Client  and set the parent account as the delgated org account
    parentAccountId = get_account_id()
    rootMacie = boto3.client('macie2')


    print('Making {0} the Macie admin account'.format(parentAccountId))

    try:
        rootMacie.enable_organization_admin_account(adminAccountId=parentAccountId)
        print('Enabling auto-enable in {0}'.format(parentAccountId))
        rootMacie.update_organization_configuration(autoEnable=True )
    except:
        pass

    for selectedAccount in selectedAccounts:
        print('Associating {0} with master account {1} and enabling Macie'.format( selectedAccount['Id'], parentAccountId))

        rootMacie.create_member(
            account={
                'accountId': selectedAccount['Id'],
                'email': selectedAccount['Email']
            },
            tags=tags
        )
    pass


if __name__ == '__main__':
    main()