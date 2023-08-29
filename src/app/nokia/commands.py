"""
Module for store comands for send in OLT
"""
commands_ssh = {
    "disable_alarms": "environment inhibit-alarms",
    "list_onu": "show equipment ont status pon | match exact:ALCL:{}"
}
