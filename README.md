# What does this do?
- Enables Macie in the root AWS organizations account
- Delegates Macie access to the AWS organization root account
- Adds child accounts to the root Macie account

# You assume all resonsibility for running this. Review the scripts carefully!

# How do I run this?
### Prerequiste
- Must have python3 installed
- Must have the latest version of boto3

### Run steps
1. Add your AWS credentials to as ENV variables, e.g. EXPORT ....
2. Run `pip3 install -r requirements.txt`
3. Run `python3 importAccounts.py`