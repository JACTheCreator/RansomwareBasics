#Category 3
import os
from cryptography.fernet import Fernet

def encrypt_file(key, file_name):
    encrypted_file_name = os.path.splitext(file_name)[0] + '_encrypted' + os.path.splitext(file_name)[1]
    with open(file_name, 'rb') as f:
        with open(encrypted_file_name, 'wb') as f_enc:
            plain_text = f.read()
            f_enc.write(plain_text)

    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text)

    with open(encrypted_file_name, 'wb') as f:
        f.write(cipher_text)
    
    os.remove(file_name)

def decrypt_file(key, file_name):
    with open(file_name, 'rb') as f:
        cipher_text = f.read()
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text)

    with open(file_name, 'wb') as f:
        f.write(plain_text)

key, file_name = b'7r128iawNRAJVPoZDcR2rh4Oz_En3XW8UboAfM4keSg=', 'Test_encrypted.txt'
encrypt_file(key, file_name)

# decrypt_file(key, file_name)
