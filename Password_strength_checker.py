import re

password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"\d", password):
    score += 1
if re.search(r"[!@#$%^&*]", password):
    score += 1

if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
