#!/bin/bash
#Instalación automática de K3s en la instancia EC2
sudo yum update -y
curl -sfL https://get.k3s.io | sh -
