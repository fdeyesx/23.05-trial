from ipaddress import *

n = ip_network('98.81.154.195/255.252.0.0',0)
for i in n:
    print(i)
