# #  v1 working delte button not working and encryption button is not there
# import os
# import json
# import hashlib
# import base64
# import sys
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.backends import default_backend
# from cryptography.fernet import Fernet
# import argparse

# # Define storage path
# STORAGE_DIR = "vault"
# META_FILE = os.path.join(STORAGE_DIR, "metadata.json")

# # Ensure storage directory exists
# os.makedirs(STORAGE_DIR, exist_ok=True)

# cipher = None  # Placeholder for the encryption object

# def derive_key(password: str, salt: bytes) -> bytes:
#     """Derives a key from the given password using PBKDF2."""
#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,
#         salt=salt,
#         iterations=100000,
#         backend=default_backend()
#     )
#     return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# def set_cipher(password: str):
#     """Sets up the encryption cipher with a user-provided password."""
#     global cipher
#     salt = b"static_salt_value"  # Consider a more secure salt handling method
#     cipher = Fernet(derive_key(password, salt))

# def load_metadata():
#     """Loads metadata from the storage file."""
#     if os.path.exists(META_FILE):
#         with open(META_FILE, "r") as meta:
#             return json.load(meta)
#     return {}

# def save_metadata(metadata):
#     """Saves metadata to the storage file."""
#     with open(META_FILE, "w") as meta:
#         json.dump(metadata, meta, indent=4)

# def encrypt_file(file_path):
#     """Encrypts and stores a file securely with versioning."""
#     if cipher is None:
#         print("Error: Encryption key is not set.")
#         return
    
#     metadata = load_metadata()
#     file_name = os.path.basename(file_path)
#     version = metadata.get(file_name, {}).get("latest_version", 0) + 1
#     enc_file_path = os.path.join(STORAGE_DIR, f"{file_name}_v{version}.enc")
    
#     with open(file_path, "rb") as f, open(enc_file_path, "wb") as ef:
#         data = f.read()
#         encrypted_data = cipher.encrypt(data)
#         ef.write(encrypted_data)
    
#     metadata.setdefault(file_name, {"latest_version": 0, "versions": {}})
#     metadata[file_name]["latest_version"] = version
#     metadata[file_name]["versions"][str(version)] = enc_file_path
    
#     save_metadata(metadata)
#     os.remove(file_path)
#     print(f"File '{file_name}' encrypted and stored as version {version}.")

# def decrypt_file(enc_file_path):
#     """Decrypts a single encrypted file."""
#     if cipher is None:
#         print("Error: Decryption key is not set.")
#         return
    
#     try:
#         with open(enc_file_path, "rb") as ef:
#             encrypted_data = ef.read()
        
#         decrypted_data = cipher.decrypt(encrypted_data)
#         decrypted_file_path = enc_file_path.replace(".enc", "").split("_v")[0]
        
#         with open(decrypted_file_path, "wb") as df:
#             df.write(decrypted_data)
        
#         os.remove(enc_file_path)
#         print(f"Decryption successful: '{decrypted_file_path}'")
#     except Exception:
#         print("Error: Decryption failed! Invalid password or corrupted file.")

# def list_files():
#     """Lists all stored files with versions."""
#     metadata = load_metadata()
#     if not metadata:
#         print("No files stored.")
#     else:
#         for file, details in metadata.items():
#             versions = ", ".join(details["versions"].keys())
#             print(f"- {file} (Versions: {versions})")

# def delete_file(file_name):
#     """Deletes a file and all its versions."""
#     metadata = load_metadata()
    
#     if file_name not in metadata:
#         print(f"File '{file_name}' not found in vault!")
#         return
    
#     for path in metadata[file_name]["versions"].values():
#         if os.path.exists(path):
#             os.remove(path)
    
#     del metadata[file_name]
#     save_metadata(metadata)
#     print(f"File '{file_name}' deleted.")

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Digital Identity Vault CLI")
#     parser.add_argument("--password", required=True, help="Password for encryption/decryption")
#     parser.add_argument("command", choices=["store", "decrypt", "list", "delete"], help="Command to execute")
#     parser.add_argument("files", nargs="*", help="File(s) to process")
#     args = parser.parse_args()
    
#     set_cipher(args.password)
    
#     if args.command == "store":
#         encrypt_file(args.files[0])
#     elif args.command == "decrypt":
#         decrypt_file(args.files[0])
#     elif args.command == "list":
#         list_files()
#     elif args.command == "delete":
#         delete_file(args.files[0])

#  v2 everything is working
import os
import json
import hashlib
import base64
import sys
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import argparse

# Define storage path
STORAGE_DIR = "vault"
META_FILE = os.path.join(STORAGE_DIR, "metadata.json")

# Ensure storage directory exists
os.makedirs(STORAGE_DIR, exist_ok=True)

cipher = None  # Placeholder for the encryption object

def derive_key(password: str, salt: bytes) -> bytes:
    """Derives a key from the given password using PBKDF2."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def set_cipher(password: str):
    """Sets up the encryption cipher with a user-provided password."""
    global cipher
    salt = b"static_salt_value"  # Consider a more secure salt handling method
    cipher = Fernet(derive_key(password, salt))

def load_metadata():
    """Loads metadata from the storage file."""
    if os.path.exists(META_FILE):
        with open(META_FILE, "r") as meta:
            return json.load(meta)
    return {}

def save_metadata(metadata):
    """Saves metadata to the storage file."""
    with open(META_FILE, "w") as meta:
        json.dump(metadata, meta, indent=4)

def encrypt_file(file_path):
    """Encrypts and stores a file securely with versioning."""
    if cipher is None:
        print("Error: Encryption key is not set.")
        return
    
    metadata = load_metadata()
    file_name = os.path.basename(file_path)
    version = metadata.get(file_name, {}).get("latest_version", 0) + 1
    enc_file_path = os.path.join(STORAGE_DIR, f"{file_name}_v{version}.enc")
    
    with open(file_path, "rb") as f, open(enc_file_path, "wb") as ef:
        data = f.read()
        encrypted_data = cipher.encrypt(data)
        ef.write(encrypted_data)
    
    metadata.setdefault(file_name, {"latest_version": 0, "versions": {}})
    metadata[file_name]["latest_version"] = version
    metadata[file_name]["versions"][str(version)] = enc_file_path
    
    save_metadata(metadata)
    os.remove(file_path)
    print(f"File '{file_name}' encrypted and stored as version {version}.")

def decrypt_file(enc_file_path):
    """Decrypts a single encrypted file."""
    if cipher is None:
        print("Error: Decryption key is not set.")
        return
    
    try:
        with open(enc_file_path, "rb") as ef:
            encrypted_data = ef.read()
        
        decrypted_data = cipher.decrypt(encrypted_data)
        decrypted_file_path = enc_file_path.replace(".enc", "").split("_v")[0]
        
        with open(decrypted_file_path, "wb") as df:
            df.write(decrypted_data)
        
        os.remove(enc_file_path)
        print(f"Decryption successful: '{decrypted_file_path}'")
    except Exception:
        print("Error: Decryption failed! Invalid password or corrupted file.")

def list_files():
    """Lists all stored files with versions."""
    metadata = load_metadata()
    if not metadata:
        print("No files stored.")
    else:
        for file, details in metadata.items():
            versions = ", ".join(details["versions"].keys())
            print(f"- {file} (Versions: {versions})")

def delete_file(file_name):
    """Deletes a file and all its versions from the vault."""
    metadata = load_metadata()

    print(f"Attempting to delete: {file_name}")
    print(f"Stored files in metadata: {metadata.keys()}")  # Debug: See stored file names

    if file_name not in metadata:
        print(f"File '{file_name}' not found in vault!")
        return
    
    # Delete all encrypted versions
    for version, path in metadata[file_name]["versions"].items():
        print(f"Checking path: {path}")  # Debug: Print file path before deletion
        if os.path.exists(path):
            os.remove(path)
            print(f"Deleted: {path}")
        else:
            print(f"File not found: {path}")

    # Remove file entry from metadata
    del metadata[file_name]
    save_metadata(metadata)

    print(f"File '{file_name}' and all versions deleted successfully.")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Digital Identity Vault CLI")
    parser.add_argument("--password", required=True, help="Password for encryption/decryption")
    parser.add_argument("command", choices=["store", "decrypt", "list", "delete"], help="Command to execute")
    parser.add_argument("files", nargs="*", help="File(s) to process")
    args = parser.parse_args()
    
    set_cipher(args.password)
    
    if args.command == "store":
        encrypt_file(args.files[0])
    elif args.command == "decrypt":
        decrypt_file(args.files[0])
    elif args.command == "list":
        list_files()
    elif args.command == "delete":
        delete_file(args.files[0])

