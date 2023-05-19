resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}
resource "aws_default_subnet" "default" {
  availability_zone = var.rds_availability_zone

  tags = {
    Name = "Default subnet"
  }
}
resource "aws_glue_connection" "rds_glue_connection" {
  name = "name_it_connection"

  connection_properties = {
    JDBC_CONNECTION_URL = "jdbc:postgresql://${var.rds_endpoint}/${var.rds_db_name}"
    PASSWORD            = var.rds_password
    USERNAME            = var.rds_username
  }

  physical_connection_requirements {
    availability_zone = var.rds_availability_zone
    security_group_id_list = [var.rds_vpc_security_group_id]
    subnet_id = aws_default_subnet.default.id
  }
}