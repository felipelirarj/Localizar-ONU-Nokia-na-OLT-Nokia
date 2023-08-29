"""
Module for open connection and send commands to OLT
"""
from netmiko import ConnectHandler


class ServiceLogin:
    """
    Class responsible for manage login in host
    """
    def __init__(self,host: str,login: str, password: str):
        """
        Init connection on host
        """
        self.host = host
        self.login = login
        self.password = password
        self.conn = ConnectHandler

    def __enter__(self):
        """
        Method for login in host
        """
        conn_data = {
        'device_type': 'alcatel_aos',
        'host': self.host,
        'username': self.login,
        'password': self.password,
        }
        self.conn = ConnectHandler(**conn_data)
        self.conn.find_prompt()
        return self.conn

    def __exit__(self,*exc):
        """
        End Connection
        """
        self.conn.disconnect()

class ServiceNokia:
    """
    Module for send commands to OLT
    """
    @staticmethod
    def search_onu(conn: ConnectHandler,serial:str):
        """
        Search ONU in OLT
        """
        serial_parse = serial[4:].upper()

        conn.send_config_set('environment inhibit-alarms')
        pesquisa = conn.send_command(f'show equipment ont status pon | match exact:ALCL:{serial_parse}')

        if f'{serial_parse}' in pesquisa:
            posicao=(pesquisa.replace('=', '').replace('-', '').replace('index table', '').replace('ontsearchstring|ontidx', '').replace('+', ''))
            print(f'ONU {serial} localizada na OLT')
            print(posicao)

        else:
            print(f'ONU {serial} nao localizada na OLT')
