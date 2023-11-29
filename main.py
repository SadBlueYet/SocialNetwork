import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from gui.login import Ui_MainWindow

from controller.verification import UserVerification



class LoginForm(QMainWindow):
    def __init__(self):
        super(LoginForm, self).__init__()
        self.check_login = False
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.accaunt_button.clicked.connect(self.swap_form)
        self.ui.registry_button.clicked.connect(self.get_user_data)

    def check_data(self, *, username: str, password: str, telephone_number: str = None) -> bool:
        bad_style = ("""border: 1px solid red;
                        width: 300px;
                        height:40px;
                        flex-shrink: 0;
                        border-radius: 20px;
                        background: #222;
                        color: #898888;""")

        good_style = ("""border: 1px solid green;
                        width: 300px;
                        height:40px;
                        flex-shrink: 0;
                        border-radius: 20px;
                        background: #222;
                        color: #898888;""")
        styles = {
            "username": bad_style if username == "" else good_style,
            "password": bad_style if password == "" else good_style,
            "number": bad_style if not self.check_login and telephone_number == "" else good_style
        }

        for field, style in styles.items():
            getattr(self.ui, f"{field}_line").setStyleSheet(style)

        return all(style == good_style for style in styles.values())

    def get_user_data(self):
        verification = UserVerification()
        if self.check_login:
            username = self.ui.username_line.text()
            password = self.ui.password_line.text()
            check = self.check_data(username=username, password=password)
            if not check:
                return
            verification.login(username=username, password=password)
        else:
            username = self.ui.username_line.text()
            password = self.ui.password_line.text()
            telephone_number = self.ui.number_line.text()
            check = self.check_data(username=username, password=password, telephone_number=telephone_number)
            if not check:
                return
            verification.registry(username=username, password=password, telephone_number=telephone_number)

    def swap_form(self):
        if not self.check_login:
            self.ui.number_line.close()
            self.ui.registry_label.setText("Вход")
            self.ui.registry_button.setText("Войти")
            self.ui.accaunt_button.setText("Зарегистрироваться")
            self.check_login = True
        else:
            self.ui.number_line.show()
            self.ui.registry_label.setText("Регистрация")
            self.ui.registry_button.setText("Зарегистрироваться")
            self.ui.accaunt_button.setText("Уже есть аккаунт?")
            self.check_login = False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec())