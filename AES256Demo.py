from Crypto.Cipher import AES

i = 0;
key = bytes()
while(i<=31):
  key = key + bytes([i])
  i+=1

data = b'JAGANNATH  SAHOO' #data must be 16 bytes

cipher = AES.new(key,AES.MODE_ECB)

msg = cipher.encrypt(data)
print("encrypted data:")
print(msg)

msg = cipher.decrypt(msg)
print("decrypted data:")
print(msg)
