# What does this do?
- Enables Amazon Macie in the root AWS organizations account
- Delegates Amazon Macie access to the AWS organization root account
- Adds child accounts to the root Amazon Macie account

# AMAZON MACIE IS NOT A FREE SERVICE
Pricing https://aws.amazon.com/macie/pricing/
# You assume all responsibility for running this. Review the scripts carefully!


# How do I run this?
### Prerequisite
- Must have python3 installed
- Must have the latest version of boto3

### Run steps
1. Add your AWS credentials to as ENV variables, e.g. EXPORT ....
2. Run `pip3 install -r requirements.txt`
3. Run `./macie-activate`