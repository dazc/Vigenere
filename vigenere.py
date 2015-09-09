#vigenere

PLAIN = "to be or not to be"
KEY = "SECURITY"

def encrypt(plain, key):
    plain = plain.replace(" ", "").upper() #cleaned up
    key_index = 0
    cipher = ''
    for i in plain:
        cipher += chr((ord(i)+ord(key[key_index])-2*65) %26 +65)
        if key_index < len(key) - 1:
            key_index += 1
        else:
            key_index = 0
    return cipher

# encrypt(PLAIN, KEY)

def decrypt(cipher, key):
    key_index = 0
    plain = ''
    for i in cipher:
        plain += chr((ord(i)-ord(key[key_index])-2*65) %26 +65)
        if key_index < len(key) - 1:
            key_index += 1
        else:
            key_index = 0
    return plain

# decrypt(encrypt(PLAIN, KEY), KEY)

def cryption(word, key, ende):
    key_index=0
    word = word.replace(" ", "").upper()

    # Set k to default as None, -1 for decrypting, or 1 for encrypting
    k = None
    if ende == 'D':
        k = -1
    elif ende == 'E':
        k = 1

    try:
        answer = '' # String to build answer
        for i in word:
            # [1]
            answer += chr((ord(i)+ord(key[key_index])*k-2*65) %26 +65)

            # Increment or reset key_index
            if key_index < len(key) - 1:
                key_index += 1
            else:
                key_index = 0
                
        return answer

    # if k is still None, it throws TypeError during [1]
    except TypeError:
        print("Choose 'E' for encryption or 'D' for decryption")

# [1]
# Append new letters to answer
#   (Numeric ASCII value for word character
#   + (Numeric ASCII value for key character
#       * k for either encrypt or decrypt)
#   - ((65 to adjust) * (2 for each ASCII value)))
#   % 26 to determine index in alphabet
#   + 65 to adjust from alphabet index to ASCII value

