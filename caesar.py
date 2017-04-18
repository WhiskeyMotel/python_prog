def encrypt_caesar(plaintext, shift):
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    ciphertext=str()
    for i in range(len(plaintext)):
        if 91<=(ord(plaintext[i])+shift)<97:
            ciphertext+=chr(64+(ord(plaintext[i])+shift)-90)
        elif (ord(plaintext[i])+shift)>122:
            ciphertext += chr(96 + (ord(plaintext[i]) + shift) - 122)
        else:
            ciphertext+=chr(ord(plaintext[i])+shift)
    return ciphertext

print(encrypt_caesar("PYTHON", 4))
print(encrypt_caesar("python",4))
print(encrypt_caesar("",3))

def decrypt_caesar(ciphertext,shift):
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    # PUT YOUR CODE HERE
    plaintext=str()
    for i in range (len(ciphertext)):
        if ord(ciphertext[i])-shift<65:
            plaintext+=chr(91-(65-(ord(ciphertext[i])-shift)))
        elif 90<ord(ciphertext[i])-shift<97:
            plaintext+=chr(123-(97-(ord(ciphertext[i])-shift)))
        else:
            plaintext+=chr(ord(ciphertext[i])-shift)
    return plaintext

print(decrypt_caesar("SBWKRQ",3))
print(decrypt_caesar("sbwkrq",3))
print(decrypt_caesar("",3))