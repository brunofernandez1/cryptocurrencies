# Write  a  function  which  computes  the  merkle  root.
import hashlib
import binascii

def hash(x):
    return hashlib.sha256(str(x).encode()).digest()

def merkle_root(datalist):
    """Returns  the  merkle  root  of  a  merkle  tree  defined  by
    the  leaves  in  datalist"""
    hashlist = [hash(x)for x in datalist  ]
    while len(hashlist)>1:
        pairs=zip(hashlist[::2],  hashlist[1::2])
        hashlist=[hash(x[0]+x[1])for x in pairs]
    return hashlist[0]

l=['I','am','Satoshi','Nakamoto']
mr=merkle_root(l)
print(binascii.hexlify(mr))