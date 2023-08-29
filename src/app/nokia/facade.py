"""
Module for facade btween Web and Service
"""
from typing import Dict
from src.app.nokia.service import ServiceLogin,ServiceNokia

class FacadeNokia:
    """
    Class Facade Nokia
    """
    def search_onu(olt:Dict):
        """
        Method for search ONU in Nokia OLT
        """
        try:
            conn = ServiceLogin(
                host=olt['olt_ip'],
                login=olt['login_ssh'],
                password=olt['ssh_pass']
            )
            with conn as connection:
                return ServiceNokia.search_onu(connection,olt['serial'])

        except Exception as err:
            return None
