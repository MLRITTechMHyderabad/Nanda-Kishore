import re

def is_strong_password(password):
    # Check length
    if len(password) < 8:
        return False
    # Check for uppercase, lowercase, digit, and special character
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@$!%*?&#]', password):
        return False
    return True

# Example passwords
passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]

# Validate each password
for pwd in passwords:
    result = "Valid" if is_strong_password(pwd) else "Invalid"
    print(f"{pwd} -> {result}")
