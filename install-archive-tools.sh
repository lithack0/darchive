#!/bin/bash

# install-archive-tools.sh
# Installs required archive extraction tools on Debian/Ubuntu systems

set -e

echo "Updating package lists..."
sudo apt update

echo "Installing archive tools..."
sudo apt install -y unzip unrar p7zip-full p7zip-rar tar

echo "All archive tools installed successfully!"
