# PUNTO 1-3
import hashlib

# We can see here the different hash algorithms that we have 
print(hashlib.algorithms_guaranteed) # Guaranteed in all platforms
print(hashlib.algorithms_available) # Available in the current interpreter

## MD5
m1 = hashlib.md5()
m1.update(b"Cloud Computing time")
print(m1.hexdigest())

## SHA1
m2 = hashlib.sha1()
m2.update(b"Cloud Computing time")
print(m2.hexdigest())

## SHA2 (224)
m3 = hashlib.sha224()
m3.update(b"Cloud Computing time")
print(m3.hexdigest())

## SHA2 (256)
m3 = hashlib.sha256()
m3.update(b"Cloud Computing time")
print(m3.hexdigest())