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

def encrypt_vigenere(plaintext, keyword):
    while len(keyword)<len(plaintext):
        keyword+=keyword
    ciphertext=str()
    for i in range (len(plaintext)):
        if 91<=(ord(plaintext[i])+find_number_letter(keyword[i]))<97:
            ciphertext+=chr(64+(ord(plaintext[i])+find_number_letter(keyword[i]))-90)
        elif (ord(plaintext[i])+find_number_letter(keyword[i]))>122:
            ciphertext += chr(96 + (ord(plaintext[i]) + find_number_letter(keyword[i])) - 122)
        else:
            ciphertext+=chr(ord(plaintext[i])+find_number_letter(keyword[i]))
    return ciphertext

print(encrypt_vigenere('MASHA', 'CA'))
print(encrypt_vigenere('masha', 'ca'))

def decrypt_vigenere(ciphertext, keyword):
    while len(keyword)<len(ciphertext):
        keyword+=keyword
    plaintext=str()
    for i in range (len(ciphertext)):
        if ord(ciphertext[i])-find_number_letter(keyword[i])<65:
            plaintext+=chr(91-(65-(ord(ciphertext[i])-find_number_letter(keyword[i]))))
        elif 90<ord(ciphertext[i])-find_number_letter(keyword[i])<97:
            plaintext+=chr(123-(97-(ord(ciphertext[i])-find_number_letter(keyword[i]))))
        else:
            plaintext+=chr(ord(ciphertext[i])-find_number_letter(keyword[i]))
    return plaintext

print(decrypt_vigenere('OAUHC','CA'))
print(decrypt_vigenere('oauhc','ca'))
