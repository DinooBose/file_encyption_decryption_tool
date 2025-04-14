import os
import argparse
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return key

def encrypt_file(input_file: str, output_file: str, password: str):
    salt = os.urandom(16)
    key = generate_key(password, salt)

    with open(input_file, 'rb') as f:
        data = f.read()

    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(salt + iv + encrypted_data)

def decrypt_file(input_file: str, output_file: str, password: str):
    with open(input_file, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted_data = f.read()

    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    with open(output_file, 'wb') as f:
        f.write(data)

def main():
    parser = argparse.ArgumentParser(description='File Encryption/Decryption Tool')
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Mode of operation')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')
    parser.add_argument('password', help='Password for encryption/decryption')

    args = parser.parse_args()

    if args.mode == 'encrypt':
        encrypt_file(args.input_file, args.output_file, args.password)
    elif args.mode == 'decrypt':
        decrypt_file(args.input_file, args.output_file, args.password)

if __name__ == '__main__':
    main()
