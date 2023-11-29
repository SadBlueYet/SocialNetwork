from dataclasses import dataclass

import json, socket

"""
    Этот класс отвечает за получение и выдачу данных пользователя
"""


@dataclass
class UserData:
    username: str
    password: str
    is_registration: bool
    telephone_number: str = None
    ip_address: str = None

    def __post_init__(self):
        self.ip_address = socket.gethostbyname(socket.gethostname())

    def serialization(self):
        return json.dumps(self.__dict__)
