#Category 1
import os
from cryptography.fernet import Fernet

def encrypt_file(key, file_name):
    new_file_location = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
    new_file_location_path = new_file_location + '\\' + os.path.basename(file_name)
    os.rename(os.path.abspath(file_name), new_file_location_path)

    with open(new_file_location_path, 'rb') as f:
        plain_text = f.read()
    
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text)

    with open(new_file_location_path, 'wb') as f:
        f.write(cipher_text)
    
    os.rename(new_file_location_path, os.path.abspath(file_name))


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

