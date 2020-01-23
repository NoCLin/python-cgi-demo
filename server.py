#! /usr/bin/env python3
# -*-coding:utf-8-*-
import argparse
import os
from http.server import CGIHTTPRequestHandler, HTTPServer


def get_ip_list():
    import socket
    return socket.gethostbyname_ex(socket.gethostname())[-1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()

    os.chdir("wwwroot")

    print("访问地址：")
    for i in get_ip_list():
        print("http://%s:%s" % (i, args.port))

    http_server = HTTPServer(("0.0.0.0", args.port), CGIHTTPRequestHandler)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
    http_server.server_close()
