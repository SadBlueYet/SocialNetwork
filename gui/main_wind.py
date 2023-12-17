import sys
import os
from random import randint


from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from gui.ui.main_gui import Ui_Message_Window
from gui.ui.chat import Ui_Chat
from gui.messanger_objects.Session import Session


#создаем виджет чата
class Chats(QWidget):
    def __init__(self, last_mes: str, count_new_mes: int, user_nick: str):
        super(Chats, self).__init__()
        self.ui = Ui_Chat()
        self.ui.setupUi(self)
        self.ui.mes_text.setText(f" {last_mes} ")
        self.ui.user_nick.setText(user_nick)
        if count_new_mes == 0:
            self.ui.new_mes.setText(f"")
        elif count_new_mes > 99:
            self.ui.new_mes.setText(f"99+")
        else:
            self.ui.new_mes.setText(f"  {count_new_mes}  ")
        
        
class Main_Wind(QMainWindow):
    def __init__(self):
        super(Main_Wind, self).__init__()
        self.ui = Ui_Message_Window()
        self.session = Session(os.getenv("login"), os.getenv("password"))
        self.session.update()
        self.ui.setupUi(self)
        for i in range(20):
            self.ui.verticalLayout.addWidget(Chats("Привет", randint(0, 2), "Саня"))
            
            
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Main_Wind()
    window.show()

    sys.exit(app.exec())