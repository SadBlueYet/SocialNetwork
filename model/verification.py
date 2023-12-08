import hashlib
import phonenumbers
import re

from database import UsersDB
from dataclasses import dataclass


@dataclass
class Data:
    username: str
    password: str
    uuid: str
    remember_me: bool
    is_registration: bool
    telephone_number: str = None


class UserVerification:
    db: UsersDB

    def __init__(self):
        self.db = UsersDB()

    def verification(self, data: Data):
        response = {'username': self.set_username(data)}

        if data.is_registration:
            response['password'] = self.check_password(data)
            response['telephone_number'] = self.set_telephone_number(data)
            if all(response.values()):
                self.add_user(data)
            return response
        else:
            response['password'] = self.checking_password_for_existence(data)
            self.update_remember_me(data)
            return response

    def update_remember_me(self, data: Data) -> None:
        self.db.update_remember_me(remember_me=data.remember_me, uuid=data.uuid)

    def add_user(self, data: Data) -> None:
        self.db.set_user(username=data.username, password=data.password, uuid=data.uuid,
                         telephone_number=data.telephone_number, remember_me=data.remember_me)

    def check_username(self, data: Data) -> bool:
        db_username = self.db.find_username(data.username)
        if db_username is None:
            return True
        return False

    def set_username(self, data: Data) -> bool:
        if data.is_registration and not self.check_username(data):
            print("Такое имя пользователя уже существует")
            return False
        if not data.is_registration and self.check_username(data):
            print("Не найдено такого пользователя")
            return False
        return True

    def check_password(self, data: Data) -> bool:
        if not re.match("^[A-Za-z0-9]{8,}$", data.password):
            return False
        data.password = hash_password(data.password)
        return True

    def checking_password_for_existence(self, data) -> bool:
        db_password = self.db.get_password(data.username)
        if db_password is None or db_password[0] != hash_password(data.password):
            return False
        else:
            return True

    def check_repetition_telephone_number(self, data: Data) -> bool:
        db_telephone_number = self.db.get_telephone_number(data.telephone_number)
        if db_telephone_number is None:
            return True
        return False

    def set_telephone_number(self, data: Data) -> bool:
        if not check_valid_telephone_number(data.telephone_number):
            return False
        if not self.check_repetition_telephone_number(data):
            return False
        return True

    def get_remember_me_from_db(self, uuid: str):
        remember_me = self.db.get_remember_me(uuid)
        return remember_me

    def get_username(self, user_id: int):
        return self.db.get_username(user_id)

    def check_user_data(self, username: str, password: str):
        return self.db.get_user_id(username, password)

    def get_user_id(self, username: str):
        return self.db.get_user_id()

def hash_password(password: str) -> str:
    hash_object = hashlib.md5()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password


def check_valid_telephone_number(telephone_number: str) -> bool:
    try:
        phone = phonenumbers.parse(telephone_number, None)
        if phonenumbers.is_valid_number(phone):
            return True
        else:
            return False
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print("Error:", str(e))
        return False


def get_remember_me_from_db(uuid: str):
    remember_me = UsersDB().get_remember_me(uuid)
    return remember_me

