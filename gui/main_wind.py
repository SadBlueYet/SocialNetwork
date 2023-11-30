import sys
from random import randint

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

from gui.main_gui import Ui_MessageWindow
from gui.chat import Ui_Chat


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
            self.ui.new_mes.setText(f" 99+ ")
        else:
            self.ui.new_mes.setText(f"  {count_new_mes}  ")
        
        
class Main_Wind(QMainWindow):
    def __init__(self):
        super(Main_Wind, self).__init__()
        self.ui = Ui_MessageWindow()
        self.ui.setupUi(self)
        for i in range(20):
            self.ui.verticalLayout.addWidget(Chats("Иди нахуй", randint(0, 2), "Саня"))
            
