def encrypt(text, shift):
    result = ""
    for ch in text:
        if 'A' <= ch <= 'Z':
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= ch <= 'z':
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print(encrypt("Hello, World!", 3))
print(decrypt("Khoor, Zruog!", 3))