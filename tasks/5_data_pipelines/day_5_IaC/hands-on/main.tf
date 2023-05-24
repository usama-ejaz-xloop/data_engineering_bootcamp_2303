terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.20.0"
    }
  }
}

provider "aws" {
  profile = var.aws_tf_profile
  region  = var.region
}

module "employees_db_rds" {
  source = "./employees_db_rds"
  db_instance_name = var.db_instance_name
}

module "glue_data_s3" {
  source      = "./glue_data_s3"
}

module "iam_role" {
  source = "./iam_role"
}

module "vpc_endpoint" {
  source = "./vpc_endpoint"
}

module "glue_catalog_database" {
  source = "./glue_catalog_database"
}

module "glue" {
  source = "./glue"
  rds_endpoint = module.employees_db_rds.rds_endpoint
  rds_username = module.employees_db_rds.rds_username
  rds_password = module.employees_db_rds.rds_password
  rds_db_name = module.employees_db_rds.rds_db_name
  rds_vpc_security_group_id = module.employees_db_rds.rds_vpc_security_group_id
  rds_availability_zone = module.employees_db_rds.rds_availability_zone
}