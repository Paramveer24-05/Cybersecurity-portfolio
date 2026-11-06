
def valid_password(password):

    if len(password) < 8:
        print("Password must be at least 8 characters")
        return False

    if any(char.isspace() for char in password):
        print("Password must not contain spaces")
        return False

    return True


def check_password(password):

    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() and not char.isspace()
           for char in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


password = input("Enter a test password: ")

if valid_password(password):
    result = check_password(password)
    print("Password strength:", result)
else:
    print("Invalid password. Try again.")
