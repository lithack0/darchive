# Darchive 📦

A powerful and intelligent Python archive extraction tool that automatically detects and extracts various archive formats with zero configuration required.

## Overview

Darchive is a simple yet robust command-line utility designed to streamline the archive extraction process. Whether you're dealing with compressed files from different sources or working with multiple archive formats, Darchive intelligently identifies the format and uses the appropriate extraction method.

## ✨ Features

- 🔍 **Smart Detection**: Automatically identifies archive types using file extensions and magic bytes
- 🎯 **Multi-Format Support**: Handles all popular archive formats seamlessly  
- 🚀 **Zero Configuration**: Works out of the box with sensible defaults
- 📁 **Flexible Extraction**: Extract to current directory or specify custom output paths
- 🛡️ **Error Handling**: Robust error handling with informative messages
- 💻 **Cross-Platform**: Works on Linux, macOS, and Windows (with appropriate tools)
- 🔧 **System Integration**: Uses native system tools for optimal performance

## 📋 Supported Formats

| Format | Extension | Tool Used | Description |
|--------|-----------|-----------|-------------|
| ZIP | `.zip` | `unzip` | Standard ZIP archives |
| RAR | `.rar` | `unrar` | WinRAR archives |
| TAR | `.tar` | `tar` | Uncompressed tar archives |
| GZIP | `.tar.gz`, `.tgz` | `tar` | Gzip-compressed tar archives |
| BZIP2 | `.tar.bz2`, `.tbz2` | `tar` | Bzip2-compressed tar archives |
| XZ | `.tar.xz`, `.txz` | `tar` | XZ-compressed tar archives |
| 7-Zip | `.7z` | `7z` | 7-Zip archives |

## 🔧 Prerequisites

Darchive requires the following system tools to be installed:

### Required Tools
- `unzip` - For ZIP archives
- `unrar` - For RAR archives  
- `tar` - For TAR-based archives
- `7z` (p7zip-full) - For 7-Zip archives
- `Python 3.6+` - Runtime environment

### Quick Install (Debian/Ubuntu/Kali)
```bash
sudo apt update
sudo apt install unzip unrar tar p7zip-full python3
```

### Install Script
We provide an automated installation script for convenience:
```bash
chmod +x install-archive-tools.sh
./install-archive-tools.sh
```

## 📥 Installation

### Method 1: Clone from GitHub

```bash
# Clone the repository
git clone https://github.com/lithack0/darchive.git
cd darchive

# Install required tools
chmod +x install-archive-tools.sh
./install-archive-tools.sh

# Run the script
python3 darchive.py <archive_file>
```

### Method 2: Debian Package Installation

```bash
# Download the package and installer
wget https://github.com/lithack0/darchive/raw/main/darchive.deb
wget https://github.com/lithack0/darchive/raw/main/install-archive-tools.sh

# Install required tools
chmod +x install-archive-tools.sh
./install-archive-tools.sh

# Install the package
sudo dpkg -i darchive.deb
# or
sudo apt install ./darchive.deb
```

### Method 3: Direct Download

Download `darchive.py` directly and run it as a standalone script:

```bash
wget https://github.com/lithack0/darchive/raw/main/darchive.py
python3 darchive.py <archive_file>
```

## 🚀 Usage

### Basic Usage

```bash
# Extract archive to current directory
python3 darchive.py -f archive.zip

# Extract to specific directory
python3 darchive.py -f archive.tar.gz -o /path/to/output/

# Using installed package
darchive -f archive.7z -o ./extracted/
```

### Advanced Examples

```bash
# Extract ZIP file to custom directory
python3 darchive.py -f documents.zip -o ~/Documents/extracted/

# Extract TAR.BZ2 archive
python3 darchive.py -f backup.tar.bz2 -o /tmp/restore/

# Extract 7z archive with specific output path
python3 darchive.py -f data.7z -o ./project/files/
```

### Command Line Options

```bash
python3 darchive.py [OPTIONS]

Required Arguments:
  -f, --file FILE       Path to the archive file to extract

Optional Arguments:
  -o, --output DIR      Output directory (default: current directory)
  -h, --help           Show help message and exit
```

## 🔍 How It Works

1. **Format Detection**: Analyzes file extension and uses `file` command for verification
2. **Tool Selection**: Chooses the appropriate extraction tool based on detected format
3. **Extraction**: Executes the extraction using system commands with proper error handling
4. **Verification**: Confirms successful extraction and reports results

## 📊 Output Examples

### Successful ZIP Extraction
```bash
$ python3 darchive.py -f documents.zip -o ./extracted/
Running: unzip documents.zip -d ./extracted/
Archive:  documents.zip
  inflating: ./extracted/readme.txt    
  inflating: ./extracted/config.json  
  inflating: ./extracted/data.csv     
Successfully extracted to ./extracted/
```

### RAR Archive Extraction
```bash
$ python3 darchive.py -f archive.rar
Running: unrar x archive.rar .
UNRAR 5.60 freeware      Copyright (c) 1993-2018 Alexander Roshal

Extracting from archive.rar

Extracting  file1.txt                                                 OK 
Extracting  file2.pdf                                                 OK 
Extracting  folder/image.png                                          OK 
All OK
Successfully extracted to .
```

### TAR.GZ Archive Extraction
```bash
$ python3 darchive.py -f backup.tar.gz -o /tmp/restore/
Running: tar xzf backup.tar.gz -C /tmp/restore/
Successfully extracted to /tmp/restore/
```

### 7-Zip Archive Extraction
```bash
$ python3 darchive.py -f data.7z -o ./output/
Running: 7z x data.7z -o./output/

7-Zip [64] 16.02 : Copyright (c) 1999-2016 Igor Pavlov : 2016-05-21
p7zip Version 16.02 (locale=en_US.UTF-8,Utf16=on,HugeFiles=on,64 bits,4 CPUs Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz (806EA),ASM,AES-NI)

Scanning the drive for archives:
1 file, 2048576 bytes (2000 KiB)

Extracting archive: data.7z
--
Path = data.7z
Type = 7z
Physical Size = 2048576
Headers Size = 122
Method = LZMA2:192k
Solid = -
Blocks = 1

Everything is Ok

Files: 15
Size:       5242880
Compressed: 2048576
Successfully extracted to ./output/
```

### Error Handling Examples

#### File Not Found
```bash
$ python3 darchive.py -f nonexistent.zip
File does not exist: nonexistent.zip
```

#### Unsupported Format
```bash
$ python3 darchive.py -f document.pdf
Unsupported or unknown archive format: application/pdf
```

#### Extraction Failure
```bash
$ python3 darchive.py -f corrupted.zip
Running: unzip corrupted.zip -d .
Archive:  corrupted.zip
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.  In the
  latter case the central directory and zipfile comment will be found on
  the last disk(s) of this archive.
unzip:  cannot find zipfile directory in one of corrupted.zip or
        corrupted.zip.zip, and cannot find corrupted.zip.ZIP, period.
Extraction failed: Command '['unzip', 'corrupted.zip', '-d', '.']' returned non-zero exit status 9
```

#### Missing Tool
```bash
$ python3 darchive.py -f archive.rar
Running: unrar x archive.rar .
/bin/sh: 1: unrar: not found
Extraction failed: Command '['unrar', 'x', 'archive.rar', '.']' returned non-zero exit status 127
```

## 🛠️ Troubleshooting

### Common Issues

**"Command not found" errors**
```bash
# Install missing tools
sudo apt install unzip unrar tar p7zip-full
```

**Permission denied**
```bash
# Make script executable
chmod +x darchive.py

# Run with appropriate permissions
sudo python3 darchive.py archive.zip
```

**Archive format not recognized**
```bash
# Force format detection
python3 darchive.py --format=zip unknown_file.dat
```

### Debug Mode

Enable verbose output for troubleshooting:
```bash
python3 darchive.py -v --debug archive.zip
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
git clone https://github.com/lithack0/darchive.git
cd darchive
python3 -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔄 Changelog

### v2.0.0
- Added intelligent format detection
- Improved error handling and user feedback  
- Added support for .txz and .tbz2 formats
- Enhanced command-line interface

### v1.5.0
- Added 7-Zip support
- Implemented dry-run functionality
- Added verbose output option

### v1.0.0
- Initial release
- Basic extraction for ZIP, RAR, and TAR formats
- Simple command-line interface


## Author's Note 💝

Greetings, digital archaeologists and compression enthusiasts! 👋

I crafted Darchive during those late-night sessions when I found myself constantly switching between different extraction tools, trying to remember the right flags for `tar`, or dealing with yet another "unsupported format" error. We've all been there - staring at a mysterious `.tar.xz` file wondering which incantation of command-line tools will finally free its contents! 🗃️✨

This tool represents my journey from frustration to automation. Every archive format supported, every edge case handled, and every user-friendly message was born from real-world pain points that I (and probably you) have experienced. I wanted to create something that would make the simple act of "just extract this file" actually... simple.

Whether you're a system administrator dealing with backup archives, a developer working with compressed packages, or a digital forensics expert analyzing evidence, I hope Darchive becomes that reliable tool in your arsenal that just works, every time.

The beauty of archives lies not just in their compression, but in their ability to preserve and transport our digital world. Each archive tells a story - of files carefully organized, of data preserved for posterity, of someone's work packaged with care. Darchive is my contribution to helping those stories unfold seamlessly.

Remember: behind every compressed file is someone's effort to organize and preserve digital content. Let's honor that by making extraction as smooth as compression should be! 📦→📁

Keep extracting, keep exploring, and may your archives always decompress without errors!

With algorithmic affection and compression compassion,  
**117h4ck** 🔓

*P.S. - If Darchive ever saves you from the "tar: invalid option" rabbit hole at 2 AM, just remember that somewhere, a fellow developer is smiling knowing they made your digital life a tiny bit easier! 🌙💻*

---

**Security Note**: Always verify the source and contents of archives before extraction, especially when dealing with files from untrusted sources. Darchive provides the tools, but digital safety is always your responsibility.
