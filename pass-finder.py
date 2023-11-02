#!/usr/bin/env python3



from sys import argv



specials = ["'", "!", "%", "^", "&", "*", "(", ")", "+", "=", "-", "_", "{", "[", "]", "}", "\\", "|", " ", "/", ">", "<", ",", ".", "`", "~", ";", ":"]

def find():
    tmp_pass = []
    f = open(argv[1], "r")
    for password in f:
        password = password.rstrip()
        if password[0].isupper() and password[-1].isdigit() and len(password) >= 20:
            for special in argv[2]:
                special = special.strip()
                if special in password:
                    #print(password)
                    tmp_pass.append(password)
                    break

    for s in specials:
        for fpass in tmp_pass:
            if s not in fpass:
                print(fpass)
        break



find()
