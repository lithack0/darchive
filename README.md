# Darchive

This is a simple Python script that automatically detects and extracts various types of archive files such as `.zip`, `.rar`, `.tar`, `.tar.gz`, `.tar.bz2`, `.tar.xz`, `.7z`, and more using the appropriate system tools.

## Features

- Auto-detects archive type using file extensions or `file` command
- Supports popular archive formats
- Simple command-line interface
- Automatically extracts contents to the specified directory

## Supported Formats

- `.zip`
- `.rar`
- `.tar`
- `.tar.gz`
- `.tar.bz2`
- `.tar.xz`
- `.7z`

## Prerequisites

Ensure the following tools are installed on your system:

- `unzip`
- `unrar`
- `tar`
- `7z` (from `p7zip-full`)
- Python 3

### Install Tools Automatically (Debian/Ubuntu/Kali)

You can use the included Bash script to install all required archive tools:

- `install-archive-tools.sh`
# Installation Guide

This guide explains how to install and run the **Darchive**.

## By Cloning the Repository

First, clone the repository to your local machine using `git`.

```bash
git clone https://github.com/lithack0/darchive.git
cd darchive
chmod +x install-archive-tools.sh
./install-archive-tools.sh
python3 darchive.py
```
## By installing .deb package.

```bash
wget https://github.com/lithack0/darchive/blob/main/darchive.deb
wget https://github.com/lithack0/darchive/blob/main/install-archive-tools.sh
chmod +x install-archive-tools.sh
./install-archive-tools.sh
dpkg -i darchive.deb or apt install ./darchive.deb
```

