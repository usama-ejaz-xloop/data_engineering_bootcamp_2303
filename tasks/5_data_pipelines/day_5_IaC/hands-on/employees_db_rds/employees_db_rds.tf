resource "aws_default_vpc" "default" {
  tags = {
    Name = "Default VPC"
  }
}

resource "aws_security_group" "rds" {
  name   = "employees_db_rds"
  vpc_id = aws_default_vpc.default.id
  ingress {
    description = "Rule for Glue Crawler"
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    self = true
  }

  ingress {
    description = "Rule for external access"
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "employees_db_rds"
  }
}

resource "aws_db_parameter_group" "employees_db" {
  name = "employeesdb"
  family = "postgres13"

  parameter {
    name = "log_connections"
    value = "1"
  }
}

resource "aws_db_instance" "employees_db" {
  identifier = var.db_instance_name
  instance_class = "db.t3.micro"
  allocated_storage = 20
  db_name = "employees_db"
  engine = "postgres"
  engine_version = "13.7"
  username = var.db_user
  password = var.db_password
  vpc_security_group_ids = [aws_security_group.rds.id]
  parameter_group_name = aws_db_parameter_group.employees_db.name
  publicly_accessible = true
  skip_final_snapshot = true
  storage_encrypted = false
  auto_minor_version_upgrade = false
  performance_insights_enabled = false
  provisioner "local-exec" {
    command = "cd employees_db_rds/db/; pip install -r requirements.txt; python3 populate_db.py"
  }
}
