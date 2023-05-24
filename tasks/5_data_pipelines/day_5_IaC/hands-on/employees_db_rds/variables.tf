variable "db_instance_name" {
  default = "employees-db"
  description = "Initial database instance name"
}

variable "db_user" {
  default = "employees_db_admin"
  description = "RDS root user name"
}

variable "db_password" {
  default = "mod4day2empl"
  description = "RDS root user password"
  sensitive   = true
}
