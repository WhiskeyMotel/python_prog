def find_number_letter(letter):
    Alphabet_big = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    Alphabet_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u',
                    'v', 'w', 'x', 'y', 'z']
    for i in range (26):
        if letter==Alphabet_big[i]:
            return int(i)
    for i in range (26):
        if letter==Alphabet_small[i]:
            return int(i)

def find_letter(number):
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    if number>26:
        for i in range(26):
            if (number-26) == i:
                return str(Alphabet[i])
    elif number<0:
        for i in range(26):
            if abs(number) == i:
                return str(Alphabet[i])
    else:
        for i in range (26):
            if number==i:
                return str(Alphabet[i])

def encrypt_vigenere(plaintext, keyword):
    while len(keyword)<len(plaintext):
        keyword+=keyword
    ciphertext=str()
    for i in range (len(plaintext)):
        ciphertext+=str(find_letter(find_number_letter(plaintext[i])+find_number_letter(keyword[i])))
    return ciphertext

print(encrypt_vigenere('MASHA', 'CA'))
print(encrypt_vigenere('masha', 'ca'))

def decrypt_vigenere(ciphertext, keyword):
    while len(keyword)<len(ciphertext):
        keyword+=keyword
    plaintext=str()
    for i in range (len(ciphertext)):
        plaintext+=str(find_letter(find_number_letter(ciphertext[i])-find_number_letter(keyword[i])))
    return plaintext

print(decrypt_vigenere('OAUHC','CA'))
