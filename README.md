Contributions are welcome! Please open an issue or submit a pull request.
# File Encryption and Decryption Tool

A simple command-line tool to encrypt and decrypt files using AES encryption.

## Features

- Encrypt files using AES encryption.
- Decrypt files using the same AES encryption.
- User-friendly command-line interface.
- Support for different file types.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/DinooBose/file_encryption_decryption_tool.git
   cd file_encryption_decryption_tool

2. Install Dependencies
   ```bash
   pip install -r requirements.txt

3. Usage Instructions
   - go to `docs/usage.md` for usage commands.

4. Testing
   - Include test cases to ensure the tool works as expected
   - Example:
     ```bash
     python -m unittest discover -s tests
     ```

# Usage Guide

To encrypt or decrypt a file, use the following command:

## Encrypt a File:
```bash
python3 file_encryption_decryption_tool.py encrypt input_file output_file your_password
```
## Decrypt a File:
```bash
python3 file_encryption_decryption_tool.py decrypt input_file output_file your_password
```
## For Help
```bash
python3 file_encryption_decryption_tool.py --help
```
