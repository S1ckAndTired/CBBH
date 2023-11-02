#!/usr/bin/env python3


from requests import post, get
from urllib.parse import quote, unquote
from binascii import hexlify
from base64 import b64decode, b64encode
from sys import argv
from hashlib import md5

def start():
    if argv[1] == "md5":
        tomd5()
    elif argv[1] == "tamper":
        tamper()
    else:
        pass


def tamper():
    cookie = argv[2]
    c_hex = hexlify(cookie.encode()).decode('ascii')
    b64_cookie = b64encode(c_hex.encode()).decode('ascii')
    f_cookie = quote(b64_cookie)
    print(f_cookie)


def tomd5():
    cookie = str(argv[2]).split(":")
    to_md51 = md5(str(cookie[0]).encode()).hexdigest()
    to_md52 = md5(str(cookie[1]).encode()).hexdigest()
    md5_cookie = str(to_md51)+":"+str(to_md52)
    tob64 = b64encode(md5_cookie.encode()).decode('ascii')
    final = quote(tob64)
    print(final)

start()
