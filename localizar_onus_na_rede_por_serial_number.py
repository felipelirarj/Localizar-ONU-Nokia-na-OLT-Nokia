
#Author: Felipe Lira
#Date: 26/02/2022

from netmiko import ConnectHandler
from datetime import datetime
import re
import time
import getpass

OLT_Teste_01='172.16.22.10'
OLT_Teste_02='172.16.22.20'
OLT_Teste_03='172.16.22.30'
OLT_Teste_04='172.16.22.40'


olts = [OLT_Teste_01,OLT_Teste_02,OLT_Teste_03,OLT_Teste_04]


index=0
print('\n\n')    
login = input('Informe o seu login: ')
senha = getpass.getpass('Informe a sua senha: ')
onu_a_ser_localizado = input("Informe o serial do equipamento a ser localizado: ").upper()
print('\n\n')  
serial_onu = onu_a_ser_localizado[4:].upper()

for x in olts:
        
    olt=olts[index]

    print(f'\nEfetuando o login na OLT {olt}\n')
    nokia = {
            'device_type': 'alcatel_aos',
            'host': olt,
            'username': login,
            'password': senha,
            }

    net_connect = ConnectHandler(**nokia)
    net_connect.find_prompt()

    inibe = net_connect.send_config_set('environment inhibit-alarms')                                                                                                                         
    pesquisa = net_connect.send_command(f'show equipment ont status pon | match exact:ALCL:{serial_onu}')

    if f'{serial_onu}' in pesquisa:
        posicao=(pesquisa.replace('=', '').replace('-', '').replace('index table', '').replace('ontsearchstring|ontidx', '').replace('+', ''))
        print(f'ONU localizada na OLT {olt}')
        print(posicao)
    
    else:
        print(f'ONU {onu_a_ser_localizado} nao localizada na OLT {olt}')
       
    net_connect.disconnect()
    
    index=index+1
