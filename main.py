import json
import re
import random
import string

# Caesar cipher encryption and decryption functions (pre-implemented)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Password strength checker function (optional)
def is_strong_password(password):
    if (len(password)>=8 and 
        re.search(r'[A-Z]',password) and
        re.search(r'[a-z]',password) and
        re.search(r'\d',password) and
        re.search(r'[!@#$%^&*(),.?":{}|<>]',password)):
            return True
    else:
        return False

# Password generator function (optional)
def generate_password(length):
     """
    Generate a random strong password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A random strong password.
    
    """
    if length<8:
        print("Password too short.Must be at least 8 characters.")
        return None
        import random
import string

def generate_password(length):
    if length < 8:
        print("密碼長度至少需要 8 個字符")
        return None
    
    
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*(),.?\":{}|<>")

    remaining_chars = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*(),.?\":{}|<>") 
                              for _ in range(length - 4))

    # 將所有部分打亂組合
    password_list = list(uppercase + lowercase + digit + special + remaining_chars)
    random.shuffle(password_list)
    password=''.join(password_list)
    return password




# Initialize empty lists to store encrypted passwords, websites, and usernames
encrypted_passwords = []
websites = []
usernames = []

# Function to add a new password 
def add_password():
    """
    Add a new password to the password manager.

    This function should prompt the user for the website, username,  and password and store them to lits with same index. Optionally, it should check password strengh with the function is_strong_password. It may also include an option for the user to
    generate a random strong password by calling the generate_password function.

    Returns:
        None
    """
    
    website=input("Enter website:")
    username=input("Enter username:")
    choice=input("Do you want to (1) enter your own password or (2) generate a strong password?
    Enter 1 or 2:")
    if choice=="1":
        password=input("Enter password:")
        if not is_strong_password(password):
            print("Warning:Your password is not strong enough!")
    elif choice=="2":
        length=int(input(:Enter desired password length(at least 8):"))
        password=generate_password(length)
        print(f"Generated password:{password}")
    encrypted=caesar_encrypt(password,shift=3)
    websites.append(website)
    usernames.append(username)
    encrypted_passwords.append(encrypted)
    print(f"Password for {website} added successfully!")
        
    

# Function to retrieve a password 
def get_password():
    
    website=input("Enter website name to retrieve password:")
    if website in websites:
        index=websites.index(website)
        username=usernames[index]
        encrypted=encrypted_passwords[index]
        password=caesar_decrypted,shift=3)
        print(f"Username:{username}")
        print(f"Password:{password}")
    else:
        print("Website not found.")
        
    

# Function to save passwords to a JSON file 
def save_passwords():
    vault=[]
    for i in range(len(websites)):
        entry={
        "website":websites[i],
        "username":usernames[i],
        "password":encrypted_passwords[i]
    vault.append(entry)
    with open("vault.txt","w") as f:
        json.dump(vault,f)
    print("Passwords saved successfully!")
    
        
 """
    Save the password vault to a file.

    This function should save passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """

    Returns:
        None
    """

# Function to load passwords from a JSON file 
def load_passwords():
    global websites,usernames,encrypted_passwords
    try:
        with open("vault.txt","r") as f:
        vault=json.load(f)
        websites=[]
        usernames=[]
        encrypted_passwords=[]
        for entry in vault:
            websites.append(entry["website"])
            usernames.append(entry["username"])
encrypted_passwords.append(entry["password"]
    except FileNotFoundError:
        print("Vault file not found.Starting with empty password vault.")
     

  # Main method
def main():
# implement user interface 

  while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Save Passwords")
    print("4. Load Passwords")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        save_passwords()
    elif choice == "4":
        passwords = load_passwords()
        print("Passwords loaded successfully!")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()
