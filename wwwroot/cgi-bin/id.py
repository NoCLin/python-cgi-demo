#! /usr/bin/env python3
# -*-coding:utf-8-*-
import codecs
import json
import os
import sys

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)


def file_read(filename, **kwargs):
    for encoding in ["utf-8", "gbk", "gb2312", "iso-8859-1", ]:
        try:
            with open(filename, encoding=encoding, **kwargs) as f:
                return f.read()
        except UnicodeDecodeError as e:
            pass
            # cgi environment
            # print("try open %s with %s encoding failed.%s" % (filename, encoding, e))

    raise IOError


client_ip = os.environ["REMOTE_ADDR"]
client_id = "查询失败"

for line in file_read("mapping.csv").splitlines()[1:]:
    sp = line.split(",")
    if sp[0] == client_ip:
        client_id = sp[1]
        break

print("Content-type: application/json")
print()

print(json.dumps({
    "ip": client_ip,
    "id": client_id
}, ensure_ascii=False))
