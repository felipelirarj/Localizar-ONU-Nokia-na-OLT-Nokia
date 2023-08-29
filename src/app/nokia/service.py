"""
Module for open connection and send commands to OLT
"""
from netmiko import ConnectHandler
from src.app.nokia.commands import commands_ssh

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
        conn.send_config_set(commands_ssh['disable_alarms'])
        search = conn.send_command(commands_ssh['list_onu'].format(serial_parse))

        if serial_parse in search:
            onu = search.split()
            data = dict(
                search_status=True,
                serial=serial,
                slot=onu[1].split('/')[2],
                pon=onu[1].split('/')[3],
                pos=onu[1].split('/')[4],
                rx_power=onu[5],
                state=onu[4]
                )
            return data
        else:
            data = dict(
                search_status=False,
                serial=serial,
                slot=None,
                pon=None,
                pos=None,
                rx_power=None,
                state=None
                )
            return data
