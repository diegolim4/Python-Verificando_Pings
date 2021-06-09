import os

with open('hosts.txt') as file:
    file = file.read()
    file = file.splitlines()

    for ip in file:
        os.system('ping ' + ip)

