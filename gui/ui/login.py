# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from gui.resource import back_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(885, 635)
        MainWindow.setMinimumSize(QSize(820, 635))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget { \n"
" border-image:url(:/back/back.PNG) 0 0 0 0 stretch stretch; \n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(-1, 70, -1, -1)
        self.username_line = QLineEdit(self.centralwidget)
        self.username_line.setObjectName(u"username_line")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username_line.sizePolicy().hasHeightForWidth())
        self.username_line.setSizePolicy(sizePolicy)
        self.username_line.setMinimumSize(QSize(0, 40))
        self.username_line.setMaximumSize(QSize(300, 16777215))
        self.username_line.setStyleSheet(u"width: 300px;\n"
"height:40px;\n"
"flex-shrink: 0;\n"
"border-radius: 20px;\n"
"background: #222;\n"
"color: #898888;\n"
"")
        self.username_line.setAlignment(Qt.AlignCenter)
        self.username_line.setClearButtonEnabled(False)

        self.gridLayout_2.addWidget(self.username_line, 0, 0, 1, 1)

        self.password_line = QLineEdit(self.centralwidget)
        self.password_line.setObjectName(u"password_line")
        sizePolicy.setHeightForWidth(self.password_line.sizePolicy().hasHeightForWidth())
        self.password_line.setSizePolicy(sizePolicy)
        self.password_line.setMinimumSize(QSize(0, 40))
        self.password_line.setStyleSheet(u"width: 300px;\n"
"height:40px;\n"
"flex-shrink: 0;\n"
"border-radius: 20px;\n"
"background: #222;\n"
"color: #898888;")
        self.password_line.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.password_line, 1, 0, 1, 1)

        self.telephone_number_line = QLineEdit(self.centralwidget)
        self.telephone_number_line.setObjectName(u"telephone_number_line")
        sizePolicy.setHeightForWidth(self.telephone_number_line.sizePolicy().hasHeightForWidth())
        self.telephone_number_line.setSizePolicy(sizePolicy)
        self.telephone_number_line.setMaximumSize(QSize(16777215, 40))
        self.telephone_number_line.setStyleSheet(u"width: 300px;\n"
"height:40px;\n"
"flex-shrink: 0;\n"
"border-radius: 20px;\n"
"background: #222;\n"
"color: #898888;\n"
"\n"
"")
        self.telephone_number_line.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.telephone_number_line, 2, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.registry_label = QLabel(self.centralwidget)
        self.registry_label.setObjectName(u"registry_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(80)
        sizePolicy1.setHeightForWidth(self.registry_label.sizePolicy().hasHeightForWidth())
        self.registry_label.setSizePolicy(sizePolicy1)
        self.registry_label.setMinimumSize(QSize(0, 70))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        self.registry_label.setFont(font)
        self.registry_label.setStyleSheet(u"color: #898888;\n"
"font-size: 35px;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;\n"
"background: none")
        self.registry_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.registry_label, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(-1, 40, -1, 0)
        self.registry_button = QPushButton(self.centralwidget)
        self.registry_button.setObjectName(u"registry_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.registry_button.sizePolicy().hasHeightForWidth())
        self.registry_button.setSizePolicy(sizePolicy2)
        self.registry_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.registry_button.setStyleSheet(u"QPushButton{\n"
"	width: 300px;\n"
"	height:40px;\n"
"	flex-shrink: 0;\n"
"	border-radius: 20px;\n"
"	background: #514777;\n"
"	color: white;\n"
"	box-shadow: 50px 50px 16px rgba(0, 0, 0, 1), 4px 4px 8px rgba(0, 0, 0, 0.2);\n"
"}\n"
"QPushButton:hover{\n"
"	background: #3E3759;\n"
"	color: #898888;\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.registry_button, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 50)
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setStyleSheet(u"color: #898888;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.checkBox)

        self.accaunt_button = QPushButton(self.centralwidget)
        self.accaunt_button.setObjectName(u"accaunt_button")
        self.accaunt_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.accaunt_button.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	color: #898888;\n"
"	background: none;\n"
"}\n"
"QPushButton:hover{\n"
"	border: none;\n"
"	color: #4A4A4A;\n"
"}")

        self.horizontalLayout.addWidget(self.accaunt_button)


        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 5, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 14, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.username_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.password_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.telephone_number_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None))
        self.registry_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
        self.registry_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043c\u043d\u0438\u0442\u044c \u043c\u0435\u043d\u044f", None))
        self.accaunt_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0436\u0435 \u0435\u0441\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
    # retranslateUi

