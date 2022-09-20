#!/usr/bin/env python3
import netmiko
from netmiko import ConnectHandler
from sys import argv

device = {
        'device_type':'mikrotik_routeros',
        'host':'192.168.0.10',
        'port':'22',
        'username':'termit+ct',
        'password':'777git.Salihov545'
        }

sshCli = ConnectHandler(**device)

#print(sshCli.find_prompt())
output = sshCli.send_command('/ip address print')
print(output)
print('*'*20)

document = argv[1]
file = open(document, 'w')
file.write(output)
file.close()
sshCli.disconnect()




with open(document, 'r') as file:
        for line in file:
            if 'ether' in line:
                line = line[5:]
                line = line.split()
                address,network,interface = line   
                print(f'{address:20}{network:15}{interface:10}')
