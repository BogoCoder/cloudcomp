# PUNTO 4
import hashlib

# We can see here the different hash algorithms that we have 
print(hashlib.algorithms_guaranteed) # Guaranteed in all platforms
print(hashlib.algorithms_available) # Available in the current interpreter

## MD5
m1 = hashlib.md5()
m1.update(b"Cloud Computing time")
print(m1.hexdigest())

m1 = hashlib.md5()
m1.update(b"Cloud Computing timesss")
print(m1.hexdigest())

m1 = hashlib.md5()
m1.update(b"Cloud Computing")
print(m1.hexdigest())

## SHA1
m2 = hashlib.sha1()
m2.update(b"Cloud Computing time")
print(m2.hexdigest())

m2 = hashlib.sha1()
m2.update(b"Cloud Computing timesss")
print(m2.hexdigest())

m2 = hashlib.sha1()
m2.update(b"Cloud Computing")
print(m2.hexdigest())

## SHA2 (224)
m3 = hashlib.sha224()
m3.update(b"Cloud Computing time")
print(m3.hexdigest())

m3 = hashlib.sha224()
m3.update(b"Cloud Computing timesss")
print(m3.hexdigest())

m3 = hashlib.sha224()
m3.update(b"Cloud Computing")
print(m3.hexdigest())

## SHA2 (256)
m3 = hashlib.sha256()
m3.update(b"Cloud Computing time")
print(m3.hexdigest())

m3 = hashlib.sha256()
m3.update(b"Cloud Computing timesss")
print(m3.hexdigest())

m3 = hashlib.sha256()
m3.update(b"Cloud Computing")
print(m3.hexdigest())

# We can see the different lengths of the hash algorithms presented. We can see that in this particular case, they are ordered in lowest to greatest.