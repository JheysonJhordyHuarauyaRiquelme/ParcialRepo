#Configuración principal de la infraestructura AWS

provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = { Name = "product-vpc" }
}

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_subnet" "public" {
  vpc_id = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  map_public_ip_on_launch = true
}

resource "aws_security_group" "k8s_sg" {
  name        = "k8s-sg"
  description = "Permite tráfico al cluster"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 32767
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "k8s_node" {
  ami = "ami-0c02fb55956c7d316"
  instance_type = "t2.medium"

  subnet_id = aws_subnet.public.id
  security_groups = [aws_security_group.k8s_sg.id]

  user_data = file("${path.module}/ec2_k3s_install.sh")

  tags = {
    Name = "k3s-node"
  }
}

output "ec2_public_ip" {
  value = aws_instance.k8s_node.public_ip
}
