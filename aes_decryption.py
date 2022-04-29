#AES decryption with EAX mode

from Crypto.Cipher import AES 

with open('enc_data.eax', 'rb') as f:
    nonce = f.read(16)
    tag = f.read(16)
    encrypt_data = f.read()
    
with open('aes_eax_key', 'rb') as f:
    key = f.read()
    
try:
    cipher = AES.new(key, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(encrypt_data, tag)
except ValueError:
    print('decrption failed. Encrypted data corrupted') 
    
with open('hsw2.xlsx', 'wb') as f:
    f.write(data)