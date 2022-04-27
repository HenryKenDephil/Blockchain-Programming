#using Pycryptodome library to implement AES
from Crypto.Cipher import AES
from secrets import token_bytes




key=token_bytes(16) # using 128bit encryption

#defining encryption method
def encrypt(msg):
    Cipher = AES.new(key, AES.MODE_EAX)
    nonce = Cipher.nonce
    Ciphertext, tag = Cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, Ciphertext, tag


#defining decryption method

def decrypt(nonce, Ciphertext, tag):
    Cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = Cipher.decrypt(Ciphertext)
    #testing the tag
    try:
        Cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False
    
    nonce, Ciphertext, tag = encrypt(input('Enter message: '))
    plaintext=decrypt(nonce, Ciphertext, tag)
    print(f'Cipher text:{Ciphertext}')
    if not plaintext:
        print('message is corrupted')
    else:
        print(f'plain text: {plaintext}')
        
    