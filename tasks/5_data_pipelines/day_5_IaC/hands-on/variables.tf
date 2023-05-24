variable "region" {
  default = "us-east-1"
}

variable "aws_tf_profile" {
  default = "tf"
}

# RDS
variable "db_instance_name" {
  # put your unique db name here, replace john-smith with your name
  default = "john-smith-employees-db"
}