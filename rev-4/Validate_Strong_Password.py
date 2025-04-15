import re

def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[@$!%*?&#]', password):
        return False
    return True

passwords = ["WeakPass", "Str0ng@Pass", "NoSpecial1", "short!1", "Secure#123"]

for pwd in passwords:
    if is_strong_password(pwd):
        print(f"{pwd} -> Valid")
    else:
        print(f"{pwd} -> Invalid")
