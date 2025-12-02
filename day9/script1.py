import boto3
import logging
import botocore.exception

iam_user = "user_name"

def get_iam_client():
    try:
        iam = botot3.client('iam')
    except botocore.exception.BotocoreError as e:
        logging.error(f'Error Creating IAM client: {e}')
        sys.exit()

def delete_iam_user(iam,user):
    try:
        if iam.get_user(UserName=user):
            response = iam.list_mfa_devices(UserName=name)
            if responses:
                logging.info(f'Found user: {user}')
            # 🔥 Final kill
                iam.delete_user(UserName=user)
                logging.info(f"✅ User '{user}' deleted successfully.")

    except iam.exceptions.NoSuchEntityException:
        logging.warning(f"User '{user}' does not exist.")
    except botocore.exceptions.ClientError as e:
        logging.error(f"AWS ClientError: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error while deleting user '{user}'")

iam = get_iam_client()
delete_iam_user(iam,iam_user)



