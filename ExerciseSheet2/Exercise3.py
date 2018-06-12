'''
Create fuctions that produce and verify proof of work for SHA256
'''
import hashlib
import sys

def hash_conc(x,y):
        """  concatenate  x  and  y,  hash  them,
        and  return  the  hash  as  an  integer.  """
        x_bytes=str(x).encode()
        print (x_bytes)
        y_bytes=str(y).encode()
        print (y_bytes)
        hash_object=hashlib.sha256(x_bytes+y_bytes)
        hash=int(hash_object.hexdigest(),16)
        return hash

def solve(p,  d):
    nonce=0
    while True:
        if hash_conc(p,  nonce)<2**(256-d):
            return nonce
        nonce + 1

def verify(p, nonce):
    hash=hash_conc(p,  nonce)
    for d in reversed(range(256)):
        if hash < 2 ** (256 - d):
            return d

if len(sys.argv)>1:
    p=sys.argv[1]
    nonce=sys.argv[2]
    print("verified  work  of  difficulty:  {}  bits"
        .format(verify(p,  nonce)))
    sys.exit()

p='satoshi nakamoto'
d=1

for d in range(256):
    nonce=solve(p,  d)
    print("puzzle:  {},  difficulty:  {},  solution:  {}"
    .format(p,d,nonce))

abc = "abc"
defe = "defe"
print (hash_conc(abc, defe))