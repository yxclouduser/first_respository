# coding=utf-8
import json
import os
import hashlib
import pickle
import time

md5_ = hashlib.md5()
from socket import *

ip_port = ("172.16.17.131", 55445)
back_log = 5
buffer_size = 1024

# tcp_client = socket(AF_INET, SOCK_STREAM)
# tcp_client.connect(ip_port)

# end_with_word = 'c2949631-4833-4360-9ffa-6ba0d2f43831'
dict1 = {"md5": "XXX", "new_name": "xiao_66775g", "token": "bm9kZTpub2RlX2FkbWluXzIwMTkwOTAzQHl1bnpoZW4="}

path = os.path.join(os.path.dirname(os.getcwd()), 'BaiduNetdisk_6.7.2.16.exe')
with open(path, 'rb') as f:
    content = f.read()

dict1['data'] = content
md5_.update(content)
dict1['md5'] = md5_.hexdigest()

end_with_word = 'c2949631-4833-4360-9ffa-6ba0d2f43831'
# mm = pickle.dumps(dict1)
# t = pickle.loads(mm)

# print type(mm)
# print type(t)

pp = json.dumps((1, 2))
print json.loads(pp)

con = pickle.dumps(dict1) + end_with_word

# con = con.strip('\n')
# con = pickle.loads(con)
# con = json.dumps(dict1) + '|||' + content + end_with_word
# print dict1, len(con), con[:10]

# print type(con)

# tcp_client.sendall(con)
#
#
# data = tcp_client.recv(buffer_size)
# print("服务器命令执行的结果是:", data.decode("utf-8"))
#
# tcp_client.close()