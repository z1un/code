import hashlib, binascii, sys

print binascii.hexlify(hashlib.new("md4", sys.argv[1].encode("utf-16le")).digest())

# python2 -c 'import hashlib,binascii; print binascii.hexlify(hashlib.new("md4", "p@Assword!123".encode("utf-16le")).digest())'
