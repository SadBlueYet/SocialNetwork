import time
from hashlib import md5
from dataclasses import dataclass

@dataclass
class Message:
    message_id: str
    sender_id: str
    message_text: str

    @property
    def id(self) -> str:
        return self.message_id
        
    @property
    def sender(self) -> str:
        return self.sender_id
        
    @property
    def text(self) -> str:
        return self.message_text


@dataclass
class User:
    user_id: str
    all_message: list[Message] = None
    
    def __post__init__(self):
        self.all_message = []
    
    @property
    def id(self) -> str:
        return self.user_id
        
    @property
    def messages(self) -> list[Message]:
        return self.all_message
    
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


#класс для сессии
class Session:
    session_id: str
    session_user: User  #поле user - это поле нашего текущего юзера
    all_users: list[Message]
    
    #в конструкторе по айди нашего юзера создаем его инстанс и присваиваем в self.user
    def __init__(self, user_id: str):
        self.session_user = User(user_id)
        self.all_users = []
    
    @property
    def id(self) -> str:
        return self.session_id
        
    @property
    def user(self) -> User:
        return self.session_user
    
    @property
    def users(self) -> list[User]:
        return self.all_users
    
    def get_user_by_id(self, user_id: str) -> User | None:
        """
        
        метод проверяет по айди юзера есть ли этот юзер сейчас у пользователя в сессии
        
        """
        for user in self.all_users:
            if user.id == user_id:
                return user
        return None
        
    def add_user(self, user: User) -> None:
        """
        
        метод для добавления нового юзера сессии
        
        """
        self.all_users.append(user)
        
        

#эмулируем результаты первого запроса к бд
FIRST_REQUEST = {
    #ключ - айди собеседника, значение - список сообщений
    "0001" : [
        #1 значение - айди сообщения, он уникален только в рамке нашего чата
        #2 значение - айди отправителя
        #3 значение - текст сообщения
        ["0001", "0001", "ку"],
        ["0002", "0000", "привет, ты кто?"],
        ["0003", "0001", "че даун?"]
        
    ],
    #ключ - айди собеседника, значение - список сообщений
    "0002" : [
        #1 значение - айди сообщения, он уникален только в рамке нашего чата
        #2 значение - айди отправителя
        #3 значение - текст сообщения
        ["0001", "0000", "ма купи пельмениии"],
        ["0002", "0002", "а ты посуду помыл?"]
    ]
}


#эмулируем результаты второго запроса к бд
SECOND_REQUEST = {
    #ключ - айди собеседника, значение - список сообщений
    "0001" : [
        #1 значение - айди сообщения, он уникален только в рамке нашего чата
        #2 значение - айди отправителя
        #3 значение - текст сообщения
        ["0001", "0001", "ку"],
        ["0002", "0000", "привет, ты кто?"],
        ["0003", "0001", "че даун?"],
        ["0004", "0001", "че игноришь?"]
        
    ],
    #ключ - айди собеседника, значение - список сообщений
    "0002" : [
        #1 значение - айди сообщения, он уникален только в рамке нашего чата
        #2 значение - айди отправителя
        #3 значение - текст сообщения
        ["0001", "0000", "ма купи пельмениии"],
        ["0002", "0002", "а ты посуду помыл?"],
        ["0003", "0002", "и уборку сделал?"]
    ]
}
    

def get_user_id(password: str, login: str) -> str:
    """
    
    функция для получения айди юзера по его логину и закодированому паролю
    
    """
    id = "0000"
    
    #id = db.get_id(md5(password.encode(), login()))
    #примерный запрос для бд:
    #('SELECT user_id FROM users WHERE password = ? & login = ?', (password, login))
    
    return id


def get_data(user_id: str, test = None) -> dict[dict[list[str]]]:
    """
    
    функция для получения всей истории переписов юзера
    
    """
    if not test: data = FIRST_REQUEST
    else: data = SECOND_REQUEST
    
    #data = db.get_all_data(user_id)
    #примерный запрос для бд:
    #('SELECT user_id FROM chats WHERE recipient = ?', (user_id,))
    #затем пройдемя по айдишникам собеседника (sender) и получим их сообщения:
    #('SELECT message_id, sender_id, text FROM messages WHERE sender_id = ? & recipient = ?', (sender, user_id))
    
    return data
    
    
def update_data(session: Session, data: dict[dict[list[str]]]) -> None:
    #проходим по всем юзерам и их списку сообщений
    for user_id, messages in zip(data, data.values()):
        user_from_session = None
        #если сейчас такого юзера нет в сессии, мы его добавляем
        if session.get_user_by_id(user_id) is None:
            user_from_session = User(user_id)
            session.add_user(user_from_session)
        else:
            user_from_session = session.get_user_by_id(user_id)
        
        #проходимся по всем сообщениям у юзера
        for message_data in messages:
            #если это сообщение есть у юзера пропускаем
            if user_from_session.get_message_by_id(message_data[0]) is not None:
                continue
            # в ином случае добавляем
            message_id = message_data[0]
            sender_id = message_data[1]
            text = message_data[2]
            user_from_session.add_message(Message(message_id, sender_id, text))
            

def print_data(session: Session) -> None:
    print(f"чаты юзера {session.user.id}")
    
    for user in session.users:
        print(f"чат с юзером {user.id}:\n")
        for message in user.messages:
            text = ""
            if message.sender == session.user.id:
                text += "Вы: "
            else:
                text += f"{user.id}: "
            text += message.text
            print(f"{text}\n")
        print("\n\n")


if __name__ == "__main__":
    password = "hui" #lineedit1.text
    login = "12912988" #lineedit2.text
    session = Session(get_user_id(password, login))
    
    data1 = get_data(session.user.id, 0)
    update_data(session, data1)
    print_data(session)
    
    data2 = get_data(session.user.id, 1)
    update_data(session, data2)
    print_data(session)