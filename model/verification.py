import hashlib
import phonenumbers
import re

from database import UsersDB


class UserVerification:
    username: str
    password: str
    telephone_number: str
    uuid: str
    remember_me: bool
    is_registration: bool
    db: UsersDB

    def __init__(self, username: str, password: str, is_registration: bool,
                 remember_me: bool, uuid: str, telephone_number: str = None):
        self.username = username
        self.password = password
        self.uuid = uuid
        self.is_registration = is_registration
        self.remember_me = remember_me
        self.telephone_number = telephone_number
        self.db = UsersDB()

    def verification(self):
        response = {'username': self.set_username()}

        if self.is_registration:
            response['password'] = self.check_password()
            response['telephone_number'] = self.set_telephone_number()
            if all(response.values()):
                self.add_user()
            return response
        else:
            response['password'] = self.checking_password_for_existence()
            self.update_remember_me()
            return response

    def update_remember_me(self) -> None:
        self.db.update_remember_me(remember_me=self.remember_me, uuid=self.uuid)

    def add_user(self):
        self.db.set_user(username=self.username, password=self.password, uuid=self.uuid,
                         telephone_number=self.telephone_number, remember_me=self.remember_me)

    def check_username(self):
        db_username = self.db.find_username(self.username)
        a = db_username.fetchone()
        if a is None:
            return True
        else:
            return False

    def set_username(self) -> bool:
        if self.is_registration and not self.check_username():
            print("Такое имя пользователя уже существует")
            return False
        if not self.is_registration and self.check_username():
            print("Не найдено такого пользователя")
            return False
        return True

    def check_password(self) -> bool:
        if not re.match("^[A-Za-z0-9]{8,}$", self.password):
            return False
        self.password = hash_password(self.password)
        return True

    def checking_password_for_existence(self) -> bool:
        db_password = self.db.find_password(self.username)
        if db_password is None or db_password[0] != hash_password(self.password):
            return False
        else:
            return True

    def check_repetition_telephone_number(self) -> bool:
        db_telephone_number = self.db.find_telephone_number(self.telephone_number)
        a = db_telephone_number.fetchone()
        if a is None:
            return True
        else:
            return False

    def set_telephone_number(self) -> bool:
        if not check_valid_telephone_number(self.telephone_number):
            return False
        if not self.check_repetition_telephone_number():
            return False
        return True


def hash_password(password: str) -> str:
    hash_object = hashlib.sha256()
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
