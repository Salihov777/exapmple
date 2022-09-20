#!/usr/bin/env python3
import netmiko
from netmiko import ConnectHandler
from sys import argv

device = {
        'device_type':'mikrotik_routeros',
        'host':'192.168.0.10',
        'port':'22',
        'username':'termit+ct',
        'password':'.Salihov545'
        }

sshCli = ConnectHandler(**device)

output = sshCli.send_command('/ip dhcp-server lease print')

document = argv[1]
file = open(document, 'w')
file.write(output)
file.close()
sshCli.disconnect()


with open(document, 'r') as file:
    for line in file:
        if 'bound' in line:
            line = line.split()[2:-1]
            print('{:17} {:20} {:16} {:10} {:>6}'.format(*line)) 
