import os

FLAG = os.environ.get('FLAG').encode()
KEY = os.urandom(4)


def encrypt(pt, key):
    key = list(key)
    ct = b''
    intm = 0
    for i, p in enumerate(pt):
        ct += bytes([key[i % len(key)] ^ p ^ intm])
        intm = p
    return ct.hex()


def decrypt(ct, key):
    # TODO : Only god know how. If you are not, get out of my path.
    pass


if __name__ == '__main__':
    encrypted_flag = encrypt(FLAG, KEY)
    print(encrypted_flag)
