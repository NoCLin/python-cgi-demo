# encoding: utf-8
from http.server import BaseHTTPRequestHandler, HTTPServer
import string


def file_read(filename, **kwargs):
    for encoding in ["utf-8", "gbk", "gb2312", "iso-8859-1", ]:
        try:
            with open(filename, encoding=encoding, **kwargs) as f:
                return f.read()
        except UnicodeDecodeError as e:
            print("try open %s with %s encoding failed.%s" % (filename, encoding, e))
    raise IOError


def get_ip_list():
    import socket
    return socket.gethostbyname_ex(socket.gethostname())[-1]


mapping = {}
print("映射关系：")
for line in file_read("mapping.csv").splitlines()[1:]:
    sp = line.split(",")
    print(sp[0], "->", sp[1])
    mapping[sp[0]] = sp[1]

index_template = string.Template(file_read("index.html"))

BIND_PORT = 8000


class SimpleHttpServer(BaseHTTPRequestHandler):
    # noinspection PyPep8Naming
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        client_ip = self.request.getpeername()[0]
        client_id = mapping.get(client_ip, "查询失败")

        response_content = index_template.safe_substitute(ip=client_ip, id=client_id)

        self.wfile.write(bytes(response_content, "utf-8"))


http_server = HTTPServer(("0.0.0.0", BIND_PORT), SimpleHttpServer)

print("访问地址：")
for i in get_ip_list():
    print("http://%s:%s" % (i, BIND_PORT))

try:
    http_server.serve_forever()
except KeyboardInterrupt:
    pass

http_server.server_close()
