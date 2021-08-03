
def encode (text, s):
    ciphered = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            ciphered += chr((ord(char) +s - 65)%26 +65)
        else:
            ciphered += chr((ord(char) +s -97)%26 +97)
    return ciphered

print(encode("sunaina",4))

def decode(text,s):
    deciphered = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            deciphered+= chr((ord(char) -s - 65)% 26 +65)
        else:
            deciphered += chr((ord(char) -s - 97)% 26 + 97)
    return deciphered

print(decode("wyremre", 4))
