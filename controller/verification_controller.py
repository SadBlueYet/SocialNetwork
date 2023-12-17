import requests
import wmi


class UserVerification:
    username: str
    password: str
    is_registration: bool
    telephone_number: str
    uuid: str

    def __init__(self, username: str, password: str, is_registration: bool, telephone_number: str = None):
        self.username = username
        self.password = password
        self.is_registration = is_registration
        self.telephone_number = telephone_number
        self.uuid = get_uuid()

    def verification(self):
        response = requests.post('http://localhost:8000/sign', json=self.__dict__)
        return response.json()


def get_uuid():
    c = wmi.WMI()
    computer_system = c.Win32_ComputerSystemProduct()[0]
    uuid = computer_system.UUID
    return uuid


