"""
Sistema de Log
"""
from datetime import datetime


def log(self, msg):
    data_hora = datetime.strftime(datetime.now(), "%d/%m/%Y %H:%M:%S")

    with open('log.txt', 'a') as log_file:
        log_file.write(f"{data_hora}: {msg}\n")
