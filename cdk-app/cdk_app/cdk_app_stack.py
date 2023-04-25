from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_s3 as s3,
    aws_rds as rds,
    aws_ec2 as ec2
)
from constructs import Construct

class CdkAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        bucket_xlsx = s3.Bucket(self, "aspendataxlsx")
        bucket_tar = s3.Bucket(self, "aspendatatar")
        vpc = ec2.Vpc(self, "mysqlVPC")
        mysql_rds = rds.DatabaseInstance(self, "aspendb",
            engine=rds.DatabaseInstanceEngine.oracle_se2(version=rds.OracleEngineVersion.VER_19_0_0_0_2020_04_R1),
            # optional, defaults to m5.large
            instance_type=ec2.InstanceType.of(ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MICRO),
            credentials=rds.Credentials.from_password("admin", "*******"), 
            vpc=vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
            )
        )
