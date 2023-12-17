from database import UsersDB


class MessageLoader:
    db: UsersDB

    def __init__(self):
        self.db = UsersDB()

    def main_method(self, username: str, password: str) -> dict:
        response = {}
        db_password = self.db.get_password(username)
        if db_password:
            if password == db_password[0]:
                user_id = self.get_user_id(username)
                if user_id:
                    user_interlocutors = self.get_user_interlocutors(user_id[0])
                    for i in user_interlocutors:
                        chat_id = self.get_users_chat_id(user_id[0], i)
                        chat_messages = self.get_chat_messages(chat_id[0])
                        response[chat_id[0]] = chat_messages
                    return response
        return {"Ты дебил": "куда лезешь"}

    def get_user_id(self, username: str) -> tuple:
        return self.db.get_user_id(username)

    def get_user_interlocutors(self, user_id: int) -> list:
        return self.db.get_user_interlocutors(user_id)

    def get_users_chat_id(self, user_id_1: int, user_id_2: int) -> list:
        return self.db.get_users_chat(user_id_1, user_id_2)

    def get_chat_messages(self, chat_id: int) -> list:
        return self.db.get_all_messages(chat_id)


class SetMessage:
    db = UsersDB
    loader: MessageLoader
    text: str
    sender_id: int
    getter_id: int

    def __init__(self, text: str, sender_id: int, getter_id: int):
        self.db = UsersDB()
        self.loader = MessageLoader()
        self.text = text
        self.sender_id = sender_id
        self.getter_id = getter_id

    def set_message(self):
        self.set_chat()
        chat_id = self.loader.get_users_chat_id(self.sender_id, self.getter_id)
        if chat_id:
            self.db.set_message(chat_id=chat_id[0], text=self.text, sender_id=self.sender_id, getter_id=self.getter_id)
            return {"Красава": "сообщение добавлено"}
        else:
            return {"Идиот": "что то не то"}

    def set_chat(self) -> None:
        self.db.set_chat(self.getter_id, self.sender_id)
