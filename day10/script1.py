# Import core CDK library and the S3 service module
from aws_cdk import core, aws_s3 as s3

# 1. Define the Stack: A Stack is the basic unit of deployment (like a CloudFormation template)
class CloudAutomationStack(core.Stack):
    """
    This Stack defines all the infrastructure resources for our automation.
    """
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # 2. Define a Resource (Construct): 
        # Instantiating this class tells CDK to create an S3 bucket.
        # It automatically gets a unique name in AWS.
        s3.Bucket(self, "MyDevOpsAutomationBucket")
        
        # --- Example of Adding Logic ---
        # if self.node.try_get_context('environment') == 'prod':
        #     s3.Bucket(self, "ProdBucket", encryption=s3.BucketEncryption.KMS_MANAGED)


# 3. Define the App: The App is the container for all your stacks
app = core.App()

# 4. Instantiate the Stack: Create an instance of our stack class
CloudAutomationStack(app, "CloudAutomationStack")

# 5. Synthesis: Generate the CloudFormation JSON/YAML template
app.synth()

print("CDK App definition complete. Use 'cdk deploy' to provision resources.")
