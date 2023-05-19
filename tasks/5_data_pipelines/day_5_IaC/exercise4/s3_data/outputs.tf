output "s3_bucket_name" {
  description = "AWS S3 bucket name"
  value = aws_s3_bucket.s3_data.id
}