import requests
import json

from gui.messanger_objects.Message import Message

#класс для юзеров
class User:
    user_id: str
    user_name: str
    user_password: str
    all_message: list[Message]
    
    def __init__(self, user_id: str, user_name: str, user_password: str | None = None):
        if user_password:
            self.check_user_data(user_name, user_password)
            self.user_password = user_password
            
        self.user_name = user_name
        self.user_id = user_id
        self.all_message = []
    
    @property
    def id(self) -> str:
        return self.user_id
        
    @property
    def name(self) -> str:
        return self.user_name
        
    @property
    def password(self) -> str:
        return self.user_password
        
    @property
    def messages(self) -> list[Message]:
        return self.all_message
    
    @staticmethod
    def check_user_data(user_name: str, user_password: str) -> bool:
        res = requests.get("http://localhost:8000/check_user", json={"username": user_name, "password" : user_password}).json()
        print(res)
        if not res.get("id"):
            raise "user not exist!"
        return True

    def get_message_by_id(self, message_id: str) -> Message | None:
        """
        
        метод проверяет по айди сообщения есть ли это сообщение сейчас у пользователя в сессии
        
        """
        for message in self.all_message:
            if message.id == message_id:
                return message
        return None
    
    def add_message(self, message: Message) -> None:
        """
        
        метод для добавления нового сообщения юзеру
        
        """
        self.all_message.append(message)
        
    def update(self, messages: list[list[str]]) -> None:
        """
        
        метод для обновления сообщений пользователя
        
        """
        for message in messages:
            if self.get_message_by_id(message[3]):
                continue
            self.add_message(Message(message[3], message[1], message[2], message[0]))