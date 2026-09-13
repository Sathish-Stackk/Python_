expression = input("Enter expression: ")

stack = []
pairs = {')': '(', ']': '[', '}': '{'}

balanced = True

for char in expression:
    if char in "([{":
        stack.append(char)

    elif char in ")]}":
        if not stack or stack.pop() != pairs[char]:
            balanced = False
            break

if stack:
    balanced = False

print("Balanced" if balanced else "Not Balanced")
