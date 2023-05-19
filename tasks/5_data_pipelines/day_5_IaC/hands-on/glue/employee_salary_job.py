# This script is created using Glue visual editor

import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(
    sys.argv,
    [
        "JOB_NAME",
        "glue_database",
        "rds_table_name",
        "s3_table_name",
        "s3_bucket_path",
        "catalog_table_name",
    ],
)
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Relational DB
RelationalDB_node1669197271057 = glueContext.create_dynamic_frame.from_catalog(
    database=args["glue_database"],
    table_name=args["rds_table_name"],
    transformation_ctx="RelationalDB_node1669197271057",
)

# Script generated for node Amazon S3
AmazonS3_node1669197204360 = glueContext.create_dynamic_frame.from_catalog(
    database=args["glue_database"],
    table_name=args["s3_table_name"],
    transformation_ctx="AmazonS3_node1669197204360",
)

# Script generated for node Rename Field
RenameField_node1669197333081 = RenameField.apply(
    frame=RelationalDB_node1669197271057,
    old_name="emp_id",
    new_name="rds_emp_id",
    transformation_ctx="RenameField_node1669197333081",
)

# Script generated for node Join
Join_node1669197296567 = Join.apply(
    frame1=RenameField_node1669197333081,
    frame2=AmazonS3_node1669197204360,
    keys1=["rds_emp_id"],
    keys2=["emp_id"],
    transformation_ctx="Join_node1669197296567",
)

# Script generated for node Change Schema (Apply Mapping)
ChangeSchemaApplyMapping_node1669197384612 = ApplyMapping.apply(
    frame=Join_node1669197296567,
    mappings=[
        ("date of joining", "string", "date_of_joining", "date"),
        ("phone number ", "string", "phone_number ", "string"),
        ("middle initial", "string", "middle_initial", "string"),
        ("user name", "string", "username", "string"),
        ("e mail", "string", "email", "string"),
        ("first name", "string", "first_name", "string"),
        ("name prefix", "string", "name_prefix", "string"),
        ("date of birth", "string", "date_of_birth", "date"),
        ("last name", "string", "last_name", "string"),
        ("ssn", "string", "ssn", "string"),
        ("password", "string", "password", "string"),
        ("emp_id", "long", "emp_id", "long"),
        ("salary", "long", "salary", "long"),
        ("raise percent", "long", "raise_percent", "long"),
        ("date", "string", "salary_date", "date"),
    ],
    transformation_ctx="ChangeSchemaApplyMapping_node1669197384612",
)

# Script generated for node Amazon S3
AmazonS3_node1669197405264 = glueContext.getSink(
    path=args["s3_bucket_path"],
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["salary_date"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1669197405264",
)
AmazonS3_node1669197405264.setCatalogInfo(
    catalogDatabase=args["glue_database"],
    catalogTableName=args["catalog_table_name"],
)
AmazonS3_node1669197405264.setFormat("glueparquet")
AmazonS3_node1669197405264.writeFrame(ChangeSchemaApplyMapping_node1669197384612)
job.commit()
