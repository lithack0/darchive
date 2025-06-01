#!/usr/bin/env python3

import argparse
import os
import sys
import subprocess
from pathlib import Path

def detect_file_type(file_path):
    """
    Detect archive type using file extension or `file` command.
    """
    name = file_path.name.lower()
    if name.endswith('.tar.gz'):
        return '.tar.gz'
    elif name.endswith('.tar.bz2'):
        return '.tar.bz2'
    elif name.endswith('.tar.xz'):
        return '.tar.xz'
    else:
        ext = file_path.suffix.lower()
        if ext in ['.zip', '.rar', '.tar', '.gz', '.bz2', '.xz', '.7z']:
            return ext

    try:
        result = subprocess.run(['file', '--mime-type', str(file_path)], capture_output=True, text=True)
        mime = result.stdout.split()[-1].strip()
        return mime
    except Exception as e:
        print(f"Error detecting file type: {e}")
        return None

def extract_file(file_path, destination):
    ext = detect_file_type(file_path)
    cmd = []

    if ext in ['.zip', 'application/zip']:
        cmd = ['unzip', str(file_path), '-d', destination]
    elif ext in ['.rar', 'application/vnd.rar']:
        cmd = ['unrar', 'x', str(file_path), destination]
    elif ext == '.tar':
        cmd = ['tar', 'xf', str(file_path), '-C', destination]
    elif ext == '.tar.gz' or ext == 'application/gzip':
        cmd = ['tar', 'xzf', str(file_path), '-C', destination]
    elif ext == '.tar.bz2' or ext == 'application/x-bzip2':
        cmd = ['tar', 'xjf', str(file_path), '-C', destination]
    elif ext == '.tar.xz' or ext == 'application/x-xz':
        cmd = ['tar', 'xJf', str(file_path), '-C', destination]
    elif ext in ['.7z', 'application/x-7z-compressed']:
        cmd = ['7z', 'x', str(file_path), f'-o{destination}']
    else:
        print(f"Unsupported or unknown archive format: {ext}")
        return

    print(f"Running: {' '.join(cmd)}")
    try:
        subprocess.run(cmd, check=True)
        print(f"Successfully extracted to {destination}")
    except subprocess.CalledProcessError as e:
        print(f"Extraction failed: {e}")

def main():
    parser = argparse.ArgumentParser(description="Auto archive extractor tool")
    parser.add_argument('-f', '--file', required=True, help="Path to the archive file")
    parser.add_argument('-o', '--output', default='.', help="Destination directory to extract")

    args = parser.parse_args()

    file_path = Path(args.file)
    output_dir = Path(args.output)

    if not file_path.exists():
        print(f"File does not exist: {file_path}")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    extract_file(file_path, str(output_dir))

if __name__ == '__main__':
    main()
