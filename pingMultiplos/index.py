import os
import time

with open('hosts.txt') as file:
    file = file.read()
    file = file.splitlines()

    for ip in file:
        os.system(f'ping {ip}')
        print('_' * 50)
        time.sleep(5)
