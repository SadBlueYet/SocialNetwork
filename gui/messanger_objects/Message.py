#класс для сообщения
class Message:
    message_id: str
    sender_id: str
    reciever_id: str
    message_text: str
    
    def __init__(self, message_id: str, sender_id: str, reciever_id: str, message_text: str):
        self.message_id = message_id
        self.sender_id = sender_id
        self.reciever_id = reciever_id
        self.message_text = message_text
        
    @property
    def id(self) -> str:
        return self.message_id
        
    @property
    def reciever(self) -> str:
        return self.reciever_id
        
    @property
    def sender(self) -> str:
        return self.sender_id
        
    @property
    def text(self) -> str:
        return self.message_text