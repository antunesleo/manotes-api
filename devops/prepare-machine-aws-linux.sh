#!/bin/bash

#Ajustando o permissionamento
yum update -y
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www

sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
sudo chkconfig docker on

sudo curl -L https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

sudo yum install -y git

cd /home/ec2-user
mkdir projects
cd projects
git clone https://github.com/antunesleo/manotes-api
cd manotes-api
cp .env.sample.docker .env
cp .env.postgres.sample .env.postgres

docker-compose up -d --build
