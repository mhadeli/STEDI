import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Read from AWS Glue Data Catalog
AWSGlueDataCatalog_node = glueContext.create_dynamic_frame.from_catalog(
    database="stedi_db",
    table_name="customer_landing_tbl",
    transformation_ctx="AWSGlueDataCatalog_node",
)

# Filter to only rows where sharewithresearchasofdate has a value
Filter_node = Filter.apply(
    frame=AWSGlueDataCatalog_node,
    f=lambda row: row["sharewithresearchasofdate"] is not None and row["sharewithresearchasofdate"] != 0,
    transformation_ctx="Filter_node",
)

# Write the filtered data to S3
output_path = "s3://your-output-bucket/path/"  # Modify with your desired output path
CustomerTrustedZone_node = glueContext.getSink(
    path=output_path,
    connection_type="s3",
    format="json",
    transformation_ctx="CustomerTrustedZone_node",
)
CustomerTrustedZone_node.writeFrame(Filter_node)

job.commit()
