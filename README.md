# xordecode

A tool for decrypting XOR-encrypted data. Written in Python 3.

## Features

- Decrypt XOR-encrypted data
- Brute force attack (tries all 256 keys)
- Support for standard input
- Support for file input
- Binary data processing

## Usage

```
usage: xordecode [-h] [-k KEY] [FILE]

This script is XOR decrypter. Supports input from file or standard input.

positional arguments:
  FILE           Original File (omit to read from standard input)

optional arguments:
  -h, --help     show this help message and exit
  -k, --key KEY  KEY (hexadecimal)
```

## Examples

### Decrypt from file
```bash
# Brute force attack (tries all keys)
xordecode encrypted_file.txt

# Decrypt with specific key
xordecode encrypted_file.txt -k 41
```

### Decrypt from standard input
```bash
# Input from pipe
echo "encrypted_data" | xordecode -k 41

# Brute force attack from standard input
echo "encrypted_data" | xordecode
```

### Binary data processing
```bash
# Decrypt binary file
xordecode binary_file.bin -k 41
```

## Installation

- Python 3.6 or higher
- pip and build tools

```bash
# Install build dependencies
pip install build

# Build the package
python -m build

# Install the built package
pip install .
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)
