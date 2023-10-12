import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1697119322469 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://stedi-project-s3/accelerometer_landing/"],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1697119322469",
)

# Script generated for node accmeter
accmeter_node1697119369326 = glueContext.write_dynamic_frame.from_catalog(
    frame=AmazonS3_node1697119322469,
    database="stedi_db",
    table_name="accelerometer_landing_",
    transformation_ctx="accmeter_node1697119369326",
)

job.commit()