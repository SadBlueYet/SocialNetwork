# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_Chat(object):
    def setupUi(self, Chat):
        if not Chat.objectName():
            Chat.setObjectName(u"Chat")
        Chat.resize(250, 65)
        Chat.setMinimumSize(QSize(250, 65))
        Chat.setMaximumSize(QSize(17777, 65))
        Chat.setCursor(QCursor(Qt.PointingHandCursor))
        Chat.setAutoFillBackground(False)
        Chat.setStyleSheet(u"QWidget#Chat{\n"
"	background-color: #2E2E2E;\n"
"}")
        self.gridLayout = QGridLayout(Chat)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Chat)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 60))
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: #3F3F3F;\n"
"	border-radius: 20px;\n"
"}")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 0, 15, 0)
        self.mes_text = QLabel(self.widget)
        self.mes_text.setObjectName(u"mes_text")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.mes_text.setFont(font)
        self.mes_text.setCursor(QCursor(Qt.PointingHandCursor))
        self.mes_text.setStyleSheet(u"QLabel#mes_text{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.mes_text.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_2.addWidget(self.mes_text, 1, 0, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 25))
        self.widget_2.setMaximumSize(QSize(16777215, 25))
        self.widget_2.setStyleSheet(u"QLabel#new_mes{\n"
"	background-color: #3F3F3F;\n"
"	border-radius: 10px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.new_mes = QLabel(self.widget_2)
        self.new_mes.setObjectName(u"new_mes")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_mes.sizePolicy().hasHeightForWidth())
        self.new_mes.setSizePolicy(sizePolicy)
        self.new_mes.setMinimumSize(QSize(0, 0))
        self.new_mes.setMaximumSize(QSize(1677777, 20))
        self.new_mes.setFont(font)
        self.new_mes.setCursor(QCursor(Qt.PointingHandCursor))
        self.new_mes.setStyleSheet(u"QLabel#new_mes{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #7563BB;\n"
"	\n"
"}")
        self.new_mes.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.new_mes, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 1, 4, 1, 1)

        self.user_nick = QLabel(self.widget)
        self.user_nick.setObjectName(u"user_nick")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.user_nick.sizePolicy().hasHeightForWidth())
        self.user_nick.setSizePolicy(sizePolicy1)
        self.user_nick.setFont(font)
        self.user_nick.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_nick.setStyleSheet(u"QLabel#user_nick{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.user_nick.setTextFormat(Qt.AutoText)
        self.user_nick.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.user_nick, 0, 1, 1, 5)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Chat)

        QMetaObject.connectSlotsByName(Chat)
    # setupUi

    def retranslateUi(self, Chat):
        Chat.setWindowTitle(QCoreApplication.translate("Chat", u"Form", None))
        self.mes_text.setText("")
        self.new_mes.setText(QCoreApplication.translate("Chat", u"0", None))
        self.user_nick.setText("")
    # retranslateUi

