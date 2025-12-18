import binascii
with open('pyproject.toml','rb') as f:
    print(binascii.hexlify(f.read(32)))
