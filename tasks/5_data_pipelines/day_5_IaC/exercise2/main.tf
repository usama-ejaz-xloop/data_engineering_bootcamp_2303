terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.39"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-central-1"
}

resource "aws_instance" "instanceA" {
  ami           = "ami-0965bd5ba4d59211c"
  instance_type = "t2.micro"
  tags = {
    Name = "ExampleEmeritusServerInstanceA"
  }
}

resource "aws_instance" "instanceB" {
  ami           = "ami-0965bd5ba4d59211c"
  instance_type = "t2.micro"
  tags = {
    Name = "ExampleEmeritusServerInstanceB"
  }
}

resource "aws_eip" "my_instance_eip" {
  vpc      = true
  instance = aws_instance.instanceA.id
}

