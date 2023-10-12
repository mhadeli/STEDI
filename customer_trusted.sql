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

# Script generated for node Amazon S3
AmazonS3_node1697115644642 = glueContext.create_dynamic_frame.from_catalog(
    database="stedi_db",
    table_name="customer_landing_tbl",
    transformation_ctx="AmazonS3_node1697115644642",
)

# Script generated for node customer_trusted
customer_trusted_node1697115676180 = Filter.apply(
    frame=AmazonS3_node1697115644642,
    f=lambda row: (row["sharewithresearchasofdate"] > 0),
    transformation_ctx="customer_trusted_node1697115676180",
)

# Script generated for node customer_trusted
customer_trusted_node1697115811990 = glueContext.write_dynamic_frame.from_catalog(
    frame=customer_trusted_node1697115676180,
    database="stedi_db",
    table_name="customer_trusted",
    transformation_ctx="customer_trusted_node1697115811990",
)

job.commit()
