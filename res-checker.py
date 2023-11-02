#!/usr/bin/env python3


from requests import post
from sys import argv


#It checks whether the username is reflected on the response
def blah():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    proxy = {"http": "http://127.0.0.1:8080"}
    f = open(argv[2], "r")
    for payload in f:
        user = str(payload.strip().split(",")[0])
        pasw = str(payload.strip().split(",")[1])
        data = {"Username": user, "Password": pasw}
        x = post(argv[1], headers=headers, data=data, proxies=proxy, allow_redirects=True)
        if user in x.text:
            print(x.status_code, user, pasw, len(x.text))

blah()
