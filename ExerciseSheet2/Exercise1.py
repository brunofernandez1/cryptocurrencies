'''
Script to find a CRC32 collision with python 3.6
Please consider that this is my first Python script
'''
import binascii, random, string
from random import *
text = 'Satoshi Nakamoto'
min_char = 0
max_char = 127
allchar = string.ascii_letters + string.punctuation + string.digits + string.whitespace

output = binascii.crc32(text.encode())
outputhex = hex(binascii.crc32(text.encode()))
print(output)
print(outputhex)
col = 0
counter = 0

while (output != col):
    counter = counter + 1
    newtext = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    col = binascii.crc32(newtext.encode())

print (newtext)