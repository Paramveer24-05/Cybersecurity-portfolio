import string

def valid_password(password):
    if len(password) < 8:
        print("PASSWORD MUST BE MINIMUM OF 8 CHARACTERS")
        return False

    if any(char.isspace() for char in password):
        print("PASSWORD MUST NOT HAVE SPACE BETWEEN CHARACTERS")
        return False

    if not any(char in string.punctuation for char in password):
        print("PASSWORD MUST CONTAIN SPECIAL SYMBOLS (LIKE @,#,$,!...)")
        return False

    return True

def check_password(password):
    score = 0
    
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Medium"
    else:
        return "Strong"



while True:
    password = input("\nWrite a new password: ")

    if valid_password(password):
        result = check_password(password)
        print(f"password : {result}")
        break 
    else:
        print("please try again")
