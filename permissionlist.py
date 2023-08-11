# import boto3
# iam_username = input("enter username:")
# # Create an IAM client using the default credentials chain
# client = boto3.client('iam')
# try:
#     # Get the user's policy list
#     response = client.list_attached_user_policies(UserName=iam_username)   
#     # Display attached policies
#     if 'AttachedPolicies' in response:
#         print(f"Policies attached to user '{iam_username}':")
#         for policy in response['AttachedPolicies']:
#             print(policy['PolicyName'])
#     else:
#         print(f"No policies attached to user '{iam_username}'.")
# except Exception as e:
#     print(f"Error: {e}")
