import sys
import os
import hashlib

from dotenv import load_dotenv
from PySide6.QtWidgets import QApplication, QMainWindow

from gui.ui.login import Ui_MainWindow
from controller.verification_controller import UserVerification
from gui.styles.styles import styles
from gui.main_wind import Main_Wind


def update_env(remember: bool, username: str, password: str):
    os.environ.setdefault('remember', str(remember))
    os.environ.setdefault('login', username)
    os.environ.setdefault('password', hash_password(password))
    with open(".env", "w") as f:
        f.write(f"remember = '{str(remember)}'\nlogin = '{username}'\npassword = '{hash_password(password)}'")
        
        
        
def hash_password(password: str) -> str:
    hash_object = hashlib.md5()
    hash_object.update(password.encode('utf-8'))
    hashed_password = hash_object.hexdigest()
    return hashed_password
    
    
class LoginForm(QMainWindow):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.message_window = None
        self.check_login = False
        
        self.ui.accaunt_button.clicked.connect(self.swap_form)
        self.ui.registry_button.clicked.connect(self.get_user_data)

    def checking_data_for_emptiness(self, *, username: str, password: str, telephone_number: str = None) -> bool:
        """

        Метод котрый делает первичную проверку данных пользоваетля на пустоту

        """
        bad_styles = {
            "username": styles['bad_style'] if username == "" else styles['good_style'],
            "password": styles['bad_style'] if password == "" else styles['good_style'],
            "telephone_number": styles['bad_style'] if not self.check_login and telephone_number == "" else styles['good_style']
        }

        for field, style in bad_styles.items():
            getattr(self.ui, f"{field}_line").setStyleSheet(style)

        return all(style == styles['good_style'] for style in bad_styles.values())

    def get_user_data(self):
        """

        Метод котрый получает данные пользователя с лэйблов и отправляет их на проверку

        """
        remember_me = self.ui.checkBox.isChecked()
        username = self.ui.username_line.text()
        password = self.ui.password_line.text()
        telephone_number = self.ui.telephone_number_line.text()
        check = self.checking_data_for_emptiness(username=username, password=password, telephone_number=telephone_number)
        is_registration = False if self.check_login else True
        if not check: return
        verification = UserVerification(username=username, password=password, is_registration=is_registration, telephone_number=telephone_number)
            
        update_env(remember_me,username, password)
        self.check_data(verification.verification())

    def check_data(self, response):
        """

        Метод котрый проверяет данные, которые отправил нам сервер
        и применяет стили для подходящих и не подходящих данных

        """
        for field, resp in response.items():
            if not resp:
                getattr(self.ui, f"{field}_line").setStyleSheet(styles["bad_style"])
            else:
                getattr(self.ui, f"{field}_line").setStyleSheet(styles["good_style"])
        if all(response.values()):
            self.view_next_form()

    def view_next_form(self):
        self.message_window = Main_Wind()
        self.message_window.show()
        self.hide()
        
    def swap_form(self):
        """

        Метод который меняет форму регистрации на форму входа и наоборот

        """
        if not self.check_login:
            self.ui.telephone_number_line.close()
            self.ui.registry_label.setText("Вход")
            self.ui.registry_button.setText("Войти")
            self.ui.accaunt_button.setText("Зарегистрироваться")
            self.ui.telephone_number_line.clear()
            self.check_login = True
        else:
            self.ui.telephone_number_line.show()
            self.ui.registry_label.setText("Регистрация")
            self.ui.registry_button.setText("Зарегистрироваться")
            self.ui.accaunt_button.setText("Уже есть аккаунт?")
            self.check_login = False


def check_remember_me() -> bool:
    return os.getenv("remember") == "True" and os.getenv("login") and os.getenv("password")
    
if __name__ == "__main__":
    app = QApplication([])
    load_dotenv()
    if check_remember_me():
        message_window = Main_Wind()
        message_window.show()
    else:
        window = LoginForm()
        window.show()
    sys.exit(app.exec())
