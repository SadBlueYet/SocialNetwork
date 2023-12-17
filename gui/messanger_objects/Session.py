import requests

from gui.messanger_objects.User import User

#класс для сессии
class Session:
    session_id: str
    #поле user - это поле нашего текущего юзера
    session_user: User
    all_users: list[User]
    
    #в конструкторе по айди нашего юзера создаем его инстанс и присваиваем в self.user
    def __init__(self, user_login: str, user_password: str):
        self.session_user = User(self.get_user_id(user_login), user_login, user_password)
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
    
    @staticmethod
    def get_user_id(user_login: str) -> str:
        return "0000"
        #res = requests.get()
    
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

    def update(self) -> None:
        """
        
        метод для обновления собеседников юзера
        
        """
        all_data = requests.get("http://localhost:8000/loading_messages", json={"username" : self.session_user.name, "password" : self.session_user.password})
        '''for user_id, data in zip(all_data.keys(), all_data.values()):
            user = get_user_by_id(user_id)
            if not user:
                user = User(user_id, data.get("user_name"))
                self.add_user(user)
            user.update(data.get("messages_data"))'''
                
        