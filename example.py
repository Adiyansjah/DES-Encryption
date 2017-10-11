from des import DES


message = 'Hello World' # The message will process every 64 bits
key = '12345678' # Remember key only take 64 bits 

des = DES()
cipher = des.encrypt(message, key)
decryption = des.decrypt(cipher, key)

print('Message: {}'.format(message))
print('Key: {}'.format(key))
print('Cipher: {}'.format(cipher))
print('Decryption Result: {}'.format(decryption))