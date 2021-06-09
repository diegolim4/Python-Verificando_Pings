import os

userIp = input('Digite o ip ou host a ser verificado: ')

# Chamando o comando system da biblioteca os

os.system(f'ping {userIp}')
