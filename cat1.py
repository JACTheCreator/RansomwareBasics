#Category 1
from cryptography.fernet import Fernet

def encrypt_file(key, file_name):
    with open(file_name, 'rb') as f:
        plain_text = f.read()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text)

    with open(file_name, 'wb') as f:
        f.write(cipher_text)

def decrypt_file(key, file_name):
    with open(file_name, 'rb') as f:
        cipher_text = f.read()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)

    with open(file_name, 'wb') as f:
        f.write(plain_text)

key, file_name = b'7r128iawNRAJVPoZDcR2rh4Oz_En3XW8UboAfM4keSg=', 'Test.jpg'
encrypt_file(key, file_name)

# decrypt_file(key, file_name)
