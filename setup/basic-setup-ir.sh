#!/bin/bash

# Basic Server Setup
printf "Updating repositories and upgrading packages...\n"
apt update
apt install -y wget apt-transport-https ca-certificates curl software-properties-common git net-tools gnupg lsb-release unzip

printf "Installing docker\n"
apt-get remove docker docker-engine docker.io containerd runc

wget https://github.com/rahbazkon/docker-installation-debs/archive/refs/tags/v1.0.0.zip

unzip v1.0.0.zip
cd docker-installation-debs-1.0.0

sudo dpkg -i ./containerd.io_1.6.21-1_amd64.deb \
  ./docker-ce_23.0.6-1~ubuntu.22.04~jammy_amd64.deb \
  ./docker-ce-cli_23.0.6-1~ubuntu.22.04~jammy_amd64.deb \
  ./docker-buildx-plugin_0.10.4-1~ubuntu.22.04~jammy_amd64.deb \
  ./docker-compose-plugin_2.17.3-1~ubuntu.22.04~jammy_amd64.deb 

echo '{"registry-mirrors": ["https://registry.docker.ir"]}' > /etc/docker/daemon.json

systemctl daemon-reload
systemctl restart docker

printf "Installing zsh, oh my zsh\n"
apt install -y zsh
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)"

