from cryptography.fernet import Fernet


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)
#
#


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("what is the master password? ")
key = load_key() + master_pwd.bytes
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ",Password:", +str(fer.encrypt(passw.encode())))


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + +str(fer.encrypt(pwd.encode())) + "\n")


while True:
    mode = input("add/view/q for quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue


'''

1. **Key Generation (Commented Out)**:
   - The commented function `write_key()` was intended to generate a new encryption key using `Fernet.generate_key()` and save it to a file named `key.key`. This is currently not active in the code.

2. **Loading the Key**:
   - The function `load_key()` opens the `key.key` file in binary read mode, reads the encryption key from it, and returns the key. It ensures the key is loaded from storage, making it available for password encryption and decryption.

3. **Master Password Input**:
   - The script prompts the user for a master password and attempts to concatenate this password (as bytes) with the loaded encryption key. However, this line `key = load_key() + master_pwd.bytes` is incorrect because `master_pwd` is a string, and it should be converted to bytes properly using `master_pwd.encode()`.

4. **Encryption Setup**:
   - An instance of `Fernet` is created with the combined key (`key`). This instance will be used to securely encrypt and decrypt passwords.

5. **Viewing Stored Passwords**:
   - The `view()` function reads entries from a file named `passwords.txt`. Each entry is expected to contain a username and an encrypted password separated by a '|'. The function decrypts each password (note: the code incorrectly attempts to encrypt instead of decrypt) and prints the username and the decrypted password.

6. **Adding New Passwords**:
   - The `add()` function prompts the user for an account name and password. It encrypts the password with the `fer` instance and appends the account name and the encrypted password (formatted as a string) to `passwords.txt`.

### Summary of Issues:
- The line that combines the loaded key with the master password is incorrect because it does not properly handle the conversion to bytes.
- In the `view()` function, there is an attempt to encrypt passwords instead of decrypting them to display correctly.
  
### Note:
The security of this code relies on the proper safeguarding of the encryption key and the master password. Thus, it is crucial not to expose these credentials.
'''
