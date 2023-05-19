variable "bucket_name" {
  description = "AWS S3 bucket name"
  default = "data-s3"
}

variable "acl_value" {
  description = "Access control list"
  default = "private"
}
