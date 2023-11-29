import socket


class Message:
    def __init__(self, text: str,
                 sender: int,
                 receiver: int,
                 message_id: int,
                 message_type: bool,
                 departure_time: str,
                 color: str = None):

        self._message_text = text
        self._message_sender = sender
        self._message_receiver = receiver
        self._message_id = message_id
        self._message_type = message_type
        self._message_departure_time = departure_time
        self._message_color = color


class SendData(Message):

    def __init__(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = ('198.168.0.158', 8000)
            self.sock.connect(self.server_address)
        except Exception as e:
            print(e)

    def __send(self):
        try:
            #self.sock.sendall(self._m)
            self.sock.close()
        except Exception as e:
            print(e)
