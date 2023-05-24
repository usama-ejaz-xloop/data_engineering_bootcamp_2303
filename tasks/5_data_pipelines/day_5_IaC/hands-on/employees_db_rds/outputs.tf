output "rds_endpoint" {
  value = aws_db_instance.employees_db.endpoint
}

output "rds_username" {
  value       = aws_db_instance.employees_db.username
  sensitive   = true
}

output "rds_password" {
  value       = aws_db_instance.employees_db.password
  sensitive   = true
}

output "rds_db_name" {
  value = aws_db_instance.employees_db.db_name
}

output "rds_vpc_security_group_id" {
  value = aws_security_group.rds.id
}

output "rds_availability_zone" {
  value = aws_db_instance.employees_db.availability_zone
}