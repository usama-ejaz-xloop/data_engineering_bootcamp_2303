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

module "s3_data" {
  source      = "./s3_data"
  bucket_name = var.bucket_name
}

output "s3_bucket_id" {
  value = module.s3_data.s3_bucket_name
}