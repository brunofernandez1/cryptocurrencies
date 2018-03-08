'''
Requires pinacl:
    pip install pynacl

Todo:
    - Install signature schema pynacl
    - generate a keypair
    - sign a message
    - very the signed message
    - tamper with the signed message and check that verification fails

'''
import nacl.utils
from nacl.public import PrivateKey, Box

#Generate a private key
privateK = PrivateKey.generate()

#Generate a fake private key
privateKFake = PrivateKey.generate()

#Get public key
publicK = privateK.public_key

#Get FAKE public key
publicKFake = privateKFake.public_key

#Object to encrypt the message
box = Box(privateK, publicK)
box2 = Box(privateK, publicKFake)

#Message to ecrypt
message = b"this message will be encrypted"

#Encrypt and decrypt message with the right public/private key
encryptedmsg = box.encrypt(message)
print("encrypted message: ", encryptedmsg)
decryptedmsg = box.decrypt(encryptedmsg)
print("decrypted message: ", decryptedmsg)

#Encrypt the message with a wrong key and try to decrypt it
encryptedmsg = box.encrypt(message)
print("encrypted message: ", encryptedmsg)

#here you get a exception because the message was encrypted with another public key
#decryptedmsg = box2.decrypt(encryptedmsg)
print("decrypted message: ", decryptedmsg)