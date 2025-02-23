# #  v1 working delte button not working and encryption button is not there
# import customtkinter as ctk
# from tkinter import filedialog, messagebox, simpledialog
# import subprocess
# import os

# # UI Setup
# ctk.set_appearance_mode("Dark")  # Dark mode
# ctk.set_default_color_theme("blue")  # Blue theme

# root = ctk.CTk()
# root.title("Digital Identity Vault")
# root.geometry("500x500")

# # Functions
# def store_file():
#     """Encrypts and stores a new file, deleting the original."""
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
#         if password:
#             result = subprocess.run(
#                 ["python3", "vault.py", "--password", password, "store", file_path],
#                 capture_output=True, text=True
#             )
#             if result.returncode == 0:
#                 messagebox.showinfo("Success", "File encrypted and stored successfully!")
#             else:
#                 messagebox.showerror("Error", f"Error: {result.stderr}")

# def decrypt_file():
#     """Decrypts a file from the vault."""
#     file_path = filedialog.askopenfilename(initialdir="vault", title="Select Encrypted File")
#     if file_path:
#         password = simpledialog.askstring("Password", "Enter decryption password:", show='*')
#         if password:
#             result = subprocess.run(
#                 ["python3", "vault.py", "--password", password, "decrypt", file_path],
#                 capture_output=True, text=True
#             )
#             if result.returncode == 0:
#                 messagebox.showinfo("Success", "File decrypted successfully!")
#             else:
#                 messagebox.showerror("Error", f"Error: {result.stderr}")

# def list_files():
#     """Lists all encrypted files in the vault after password verification."""
#     password = simpledialog.askstring("Password", "Enter password to view stored files:", show='*')
#     if password:
#         result = subprocess.run(
#             ["python3", "vault.py", "--password", password, "list"],
#             capture_output=True, text=True
#         )
#         if result.returncode == 0:
#             file_list.delete("1.0", "end")  # Clear existing text
#             file_list.insert("end", result.stdout)
#         else:
#             messagebox.showerror("Error", f"Error: {result.stderr}")

# def delete_file():
#     """Deletes a file from the vault after password verification."""
#     file_path = filedialog.askopenfilename(initialdir="vault", title="Select File to Delete")
#     if file_path:
#         file_name = os.path.basename(file_path)
#         password = simpledialog.askstring("Password", "Enter password to delete file:", show='*')
#         if password:
#             result = subprocess.run(
#                 ["python3", "vault.py", "--password", password, "delete", file_name],
#                 capture_output=True, text=True
#             )
#             if result.returncode == 0:
#                 messagebox.showinfo("Success", "File deleted successfully!")
#             else:
#                 messagebox.showerror("Error", f"Error: {result.stderr}")

# # UI Components
# frame = ctk.CTkFrame(root)
# frame.pack(pady=20, padx=20, fill="both", expand=True)

# ctk.CTkLabel(frame, text="Digital Identity Vault", font=("Arial", 20)).pack(pady=10)
# ctk.CTkButton(frame, text="Store File", command=store_file).pack(pady=5)
# ctk.CTkButton(frame, text="Decrypt File", command=decrypt_file).pack(pady=5)
# ctk.CTkButton(frame, text="Delete File", command=delete_file).pack(pady=5)
# ctk.CTkButton(frame, text="List Stored Files", command=list_files).pack(pady=5)

# ctk.CTkLabel(frame, text="Stored Files:").pack(pady=5)
# file_list = ctk.CTkTextbox(frame, height=100, width=400)
# file_list.pack(pady=5, fill="both", expand=True)

# root.mainloop()


# #  v2 only delete button not working
# import customtkinter as ctk
# from tkinter import filedialog, messagebox, simpledialog
# import subprocess
# import os

# # UI Setup
# ctk.set_appearance_mode("Dark")  # Dark mode
# ctk.set_default_color_theme("blue")  # Blue theme

# root = ctk.CTk()
# root.title("Digital Identity Vault")
# root.geometry("500x500")

# # Functions
# def store_file():
#     """Encrypts and stores a new file, deleting the original."""
#     file_path = filedialog.askopenfilename()
#     if file_path:
#         password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
#         if password:
#             result = subprocess.run(
#                 ["python3", "vault.py", "--password", password, "store", file_path],
#                 capture_output=True, text=True
#             )
#             if result.returncode == 0:
#                 messagebox.showinfo("Success", "File encrypted and stored successfully!")
#             else:
#                 messagebox.showerror("Error", f"Error: {result.stderr}")

# def encrypt_file():
#     file_path = filedialog.askopenfilename(initialdir="vault")  # Pick from vault directory
#     if file_path:
#         password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
#         if password:
#             result = subprocess.run(
#                 ["python3", "vault.py", "--password", password, "store", file_path],  # Fix: added "--password"
#                 capture_output=True, text=True
#             )
#             if result.returncode == 0:
#                 messagebox.showinfo("Success", "File encrypted and stored successfully!")
#             else:
#                 messagebox.showerror("Error", result.stderr)


# def decrypt_file():
#     """Decrypts a file from the vault."""
#     file_path = filedialog.askopenfilename(initialdir="vault", title="Select Encrypted File")
#     if file_path:
#         password = simpledialog.askstring("Password", "Enter decryption password:", show='*')
#         if password:
#             result = subprocess.run(
#                 ["python3", "vault.py", "--password", password, "decrypt", file_path],
#                 capture_output=True, text=True
#             )
#             if result.returncode == 0:
#                 messagebox.showinfo("Success", "File decrypted successfully!")
#             else:
#                 messagebox.showerror("Error", f"Error: {result.stderr}")

# def list_files():
#     """Lists all encrypted files in the vault after password verification."""
#     password = simpledialog.askstring("Password", "Enter password to view stored files:", show='*')
#     if password:
#         result = subprocess.run(
#             ["python3", "vault.py", "--password", password, "list"],
#             capture_output=True, text=True
#         )
#         if result.returncode == 0:
#             file_list.delete("1.0", "end")  # Clear existing text
#             file_list.insert("end", result.stdout)
#         else:
#             messagebox.showerror("Error", f"Error: {result.stderr}")

# def delete_file():
#     """Deletes a file from the vault after password verification."""
#     file_path = filedialog.askopenfilename(initialdir="vault", title="Select File to Delete")
#     if file_path:
#         file_name = os.path.basename(file_path)
#         password = simpledialog.askstring("Password", "Enter password to delete file:", show='*')
#         if password:
#             result = subprocess.run(
#                 ["python3", "vault.py", "--password", password, "delete", file_name],
#                 capture_output=True, text=True
#             )
#             if result.returncode == 0:
#                 messagebox.showinfo("Success", "File deleted successfully!")
#             else:
#                 messagebox.showerror("Error", f"Error: {result.stderr}")

# # UI Components
# frame = ctk.CTkFrame(root)
# frame.pack(pady=20, padx=20, fill="both", expand=True)

# ctk.CTkLabel(frame, text="Digital Identity Vault", font=("Arial", 20)).pack(pady=10)
# ctk.CTkButton(frame, text="Store File", command=store_file).pack(pady=5)
# ctk.CTkButton(frame, text="Encrypt File", command=encrypt_file).pack(pady=5)  # New Encrypt Button
# ctk.CTkButton(frame, text="Decrypt File", command=decrypt_file).pack(pady=5)
# ctk.CTkButton(frame, text="Delete File", command=delete_file).pack(pady=5)
# ctk.CTkButton(frame, text="List Stored Files", command=list_files).pack(pady=5)

# ctk.CTkLabel(frame, text="Stored Files:").pack(pady=5)
# file_list = ctk.CTkTextbox(frame, height=100, width=400)
# file_list.pack(pady=5, fill="both", expand=True)

# root.mainloop()


#  v3 everything is working fine now
import customtkinter as ctk
from tkinter import filedialog, messagebox, simpledialog
import subprocess
import os

# UI Setup
ctk.set_appearance_mode("Dark")  # Dark mode
ctk.set_default_color_theme("blue")  # Blue theme

root = ctk.CTk()
root.title("Digital Identity Vault")
root.geometry("500x500")

# Functions
def store_file():
    """Encrypts and stores a new file, deleting the original."""
    file_path = filedialog.askopenfilename()
    if file_path:
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        if password:
            result = subprocess.run(
                ["python3", "vault.py", "--password", password, "store", file_path],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                messagebox.showinfo("Success", "File encrypted and stored successfully!")
            else:
                messagebox.showerror("Error", f"Error: {result.stderr}")

def encrypt_file():
    file_path = filedialog.askopenfilename(initialdir="vault")  # Pick from vault directory
    if file_path:
        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        if password:
            result = subprocess.run(
                ["python3", "vault.py", "--password", password, "store", file_path],  # Fix: added "--password"
                capture_output=True, text=True
            )
            if result.returncode == 0:
                messagebox.showinfo("Success", "File encrypted and stored successfully!")
            else:
                messagebox.showerror("Error", result.stderr)


def decrypt_file():
    """Decrypts a file from the vault."""
    file_path = filedialog.askopenfilename(initialdir="vault", title="Select Encrypted File")
    if file_path:
        password = simpledialog.askstring("Password", "Enter decryption password:", show='*')
        if password:
            result = subprocess.run(
                ["python3", "vault.py", "--password", password, "decrypt", file_path],
                capture_output=True, text=True
            )
            if result.returncode == 0:
                messagebox.showinfo("Success", "File decrypted successfully!")
            else:
                messagebox.showerror("Error", f"Error: {result.stderr}")

def list_files():
    """Lists all encrypted files in the vault after password verification."""
    password = simpledialog.askstring("Password", "Enter password to view stored files:", show='*')
    if password:
        result = subprocess.run(
            ["python3", "vault.py", "--password", password, "list"],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            file_list.delete("1.0", "end")  # Clear existing text
            file_list.insert("end", result.stdout)
        else:
            messagebox.showerror("Error", f"Error: {result.stderr}")

def delete_file():
    """Prompts user to select a file and delete it from the vault."""
    file_path = filedialog.askopenfilename(initialdir="vault")  
    if file_path:
        file_name = os.path.basename(file_path).split("_v")[0]  # Ensure correct filename format
        print(f"UI selected file for deletion: {file_name}")  # Debugging

        password = simpledialog.askstring("Password", "Enter encryption password:", show='*')
        if password:
            result = subprocess.run(
                ["python3", "vault.py", "--password", password, "delete", file_name], 
                capture_output=True, text=True
            )
            print(f"Subprocess output: {result.stdout}")  # Debugging
            print(f"Subprocess error (if any): {result.stderr}")

            if result.returncode == 0:
                messagebox.showinfo("Success", "File deleted successfully!")
            else:
                messagebox.showerror("Error", result.stderr)

# UI Components
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20, fill="both", expand=True)

ctk.CTkLabel(frame, text="Digital Identity Vault", font=("Arial", 20)).pack(pady=10)
ctk.CTkButton(frame, text="Store File", command=store_file).pack(pady=5)
ctk.CTkButton(frame, text="Encrypt File", command=encrypt_file).pack(pady=5)  # New Encrypt Button
ctk.CTkButton(frame, text="Decrypt File", command=decrypt_file).pack(pady=5)
ctk.CTkButton(frame, text="Delete File", command=delete_file).pack(pady=5)
ctk.CTkButton(frame, text="List Stored Files", command=list_files).pack(pady=5)

ctk.CTkLabel(frame, text="Stored Files:").pack(pady=5)
file_list = ctk.CTkTextbox(frame, height=100, width=400)
file_list.pack(pady=5, fill="both", expand=True)

root.mainloop()