import socket

from model.user_data import UserData


class SendData:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_address = ('localhost', 12345)
        self.sock.connect(self.server_address)

    def send(self, user_data):
        self.sock.sendall(user_data.encode())

        data = self.sock.recv(1024)
        return data

    def disconnect(self):
        self.sock.close()


class UserVerification:
    send: SendData

    def __init__(self):
        self.send = SendData()

    def registry(self, username: str, password: str, telephone_number: str) -> None:
        data: UserData = UserData(username=username,
                                  password=password,
                                  telephone_number=telephone_number,
                                  is_registration=True)

        body = self.send.send(data.serialization())

        if body.decode() == "0":
            print("Неправильное имя пользователя")
        elif body.decode() == "1":
            print("Неправильный пароль")
        elif body.decode() == "2":
            print("Неправильный номер телефона")
        else:
            print(body.decode())
        self.send.disconnect()

    def login(self, username: str, password: str) -> None:
        data: UserData = UserData(username=username,
                                  password=password,
                                  is_registration=False)

        body = self.send.send(data.serialization())
        if body.decode() == "0":
            print("Неправильное имя пользователя")
        elif body.decode() == "1":
            print("Неправильный пароль")
        else:
            print(body.decode())
        self.send.disconnect()
