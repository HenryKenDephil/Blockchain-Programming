#using Pycryptodome library to implement AES (EAX mode)
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

with open('aes_eax_key', 'wb') as f:
    f.write(key)
    
cipher = AES.new(key, AES.MODE_EAX)

with open('hsw.xlsx', 'rb') as f:
    data = f.read()
    
encrypt_data, tag = cipher.encrypt_and_digest(data)

with open('enc_data.eax', 'wb') as f:
    f.write(cipher.nonce)
    f.write(tag)
    f.write(encrypt_data)


