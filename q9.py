def encrypt(text, shift):
    encrypted = []
    for char in text:
        if char.isupper():
            base = ord("A")
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted.append(new_char)
        elif char.islower():
            base = ord("a")
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted.append(new_char)
        else:
            encrypted.append(char)

    return "".join(encrypted)

x=input("Enter the string to be encrypted: ")
shift = int(input("Enter the shift value: "))
print("Encrypted string:", encrypt(x, shift))