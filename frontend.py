# Created by: PyQt5 UI code generator 5.15.6
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setFamily("Microsoft Tai Le")
        Form.setFont(font)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 40, 720, 525))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        self.stackedWidget.setFont(font)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_game = QtWidgets.QWidget()
        self.page_game.setObjectName("page_game")
        self.label_question = QtWidgets.QLabel(self.page_game)
        self.label_question.setGeometry(QtCore.QRect(0, 100, 711, 150))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_question.setFont(font)
        self.label_question.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                          "color: rgb(249, 242, 232);\n"
                                          "padding: 10px")
        self.label_question.setAlignment(QtCore.Qt.AlignCenter)
        self.label_question.setWordWrap(True)
        self.label_question.setObjectName("label_question")
        self.label_17 = QtWidgets.QLabel(self.page_game)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 711, 525))
        self.label_17.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, \n"
            "stop:0 rgb(229, 153, 163), stop:1 rgb(70, 63, 125));\n"
            "border-radius: 40px;")
        self.label_17.setObjectName("label_17")
        self.button_answer1 = QtWidgets.QPushButton(self.page_game)
        self.button_answer1.setGeometry(QtCore.QRect(10, 300, 340, 60))
        self.button_answer1.setObjectName("button_answer1")
        self.button_answer4 = QtWidgets.QPushButton(self.page_game)
        self.button_answer4.setGeometry(QtCore.QRect(360, 380, 340, 60))
        self.button_answer4.setObjectName("button_answer4")
        self.button_answer2 = QtWidgets.QPushButton(self.page_game)
        self.button_answer2.setGeometry(QtCore.QRect(360, 300, 340, 60))
        self.button_answer2.setObjectName("button_answer2")
        self.button_answer3 = QtWidgets.QPushButton(self.page_game)
        self.button_answer3.setGeometry(QtCore.QRect(10, 380, 340, 60))
        self.button_answer3.setObjectName("button_answer3")
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        answer_buttons = [self.button_answer1, self.button_answer2, self.button_answer3, self.button_answer4]
        for button in answer_buttons:
            button.setFont(font)
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            name = button.objectName()
            button.setStyleSheet(f"QPushButton#{name}"
                                 "{\n"
                                 "background-color:rgb(77, 56, 76);\n"
                                 "color: \'white\';\n"
                                 "border-radius: 7px;\n"
                                 "}\n"
                                 f"QPushButton#{name}:hover"
                                 "{\n"
                                 "background-color:rgb(226, 151, 162);\n"
                                 "}\n"
                                 f"QPushButton#{name}:disabled"
                                 "{\n"
                                 "background-color:rgba(0, 0, 0, 100);\n"
                                 "color:rgb(170, 0, 0);\n"
                                 "}")

        self.button_back = QtWidgets.QPushButton(self.page_game)
        self.button_back.setGeometry(QtCore.QRect(10, 470, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button_back.setFont(font)
        self.button_back.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_back.setStyleSheet("QPushButton#button_back{\n"
                                       "background-color:rgba(0, 0, 0, 0);\n"
                                       "color: \'white\';\n"
                                       "border-radius: 7px;\n"
                                       "}\n"
                                       "QPushButton#button_back:hover{\n"
                                       "color:rgb(77, 56, 76);\n"
                                       "}\n"
                                       "QPushButton#button_back:pressed{\n"
                                       "padding-top:5px;\n"
                                       "padding-left:5px;\n"
                                       "}")
        self.button_back.setObjectName("button_back")
        self.label_score = QtWidgets.QLabel(self.page_game)
        self.label_score.setGeometry(QtCore.QRect(600, 30, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_score.setFont(font)
        self.label_score.setStyleSheet("color: white;")
        self.label_score.setObjectName("label_score")

        self.label_s = QtWidgets.QLabel(self.page_game)
        self.label_s.setGeometry(QtCore.QRect(510, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_s.setFont(font)
        self.label_s.setStyleSheet("color: white;")
        self.label_s.setObjectName("label_s")

        self.label_17.raise_()
        self.label_question.raise_()
        self.button_answer1.raise_()
        self.button_answer4.raise_()
        self.button_answer2.raise_()
        self.button_answer3.raise_()
        self.button_back.raise_()
        self.label_score.raise_()
        self.label_s.raise_()
        self.stackedWidget.addWidget(self.page_game)
        self.page_win = QtWidgets.QWidget()
        self.page_win.setObjectName("page_win")
        self.label_18 = QtWidgets.QLabel(self.page_win)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 711, 525))
        self.label_18.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 rgb(229, 153, 163), "
            "stop:1 rgb(70, 63, 125));\n"
            "border-radius: 40px;")
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.button_home = QtWidgets.QPushButton(self.page_win)
        self.button_home.setGeometry(QtCore.QRect(130, 350, 451, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button_home.setFont(font)
        self.button_home.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_home.setStyleSheet("QPushButton#button_home{\n"
                                       "background-color:rgb(77, 56, 76);\n"
                                       "color: \'white\';\n"
                                       "border-radius: 7px;\n"
                                       "}\n"
                                       "QPushButton#button_home:hover{\n"
                                       "background-color:rgb(226, 151, 162);\n"
                                       "}\n"
                                       "QPushButton#button_home:pressed{\n"
                                       "padding-top:5px;\n"
                                       "padding-left:5px;\n"
                                       "}")
        self.button_home.setObjectName("button_home")
        self.label_19 = QtWidgets.QLabel(self.page_win)
        self.label_19.setGeometry(QtCore.QRect(0, 110, 390, 151))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                    "color: rgb(249, 242, 232);\n"
                                    "padding: 10px")
        self.label_19.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_19.setWordWrap(True)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.page_win)
        self.label_20.setGeometry(QtCore.QRect(390, 110, 321, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                    "color: rgb(249, 242, 232);\n"
                                    "padding-right: 10px;\n"
                                    "padding-bottom: 5px;")
        self.label_20.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.label_score_win = QtWidgets.QLabel(self.page_win)
        self.label_score_win.setGeometry(QtCore.QRect(390, 190, 321, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_score_win.setFont(font)
        self.label_score_win.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                           "color: rgb(249, 242, 232);\n"
                                           "padding-right: 10px;\n"
                                           "color:rgb(85, 255, 0);")
        self.label_score_win.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.label_score_win.setWordWrap(True)
        self.label_score_win.setObjectName("label_score_win")
        self.stackedWidget.addWidget(self.page_win)
        self.page_lose = QtWidgets.QWidget()
        self.page_lose.setObjectName("page_lose")
        self.label_21 = QtWidgets.QLabel(self.page_lose)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 711, 525))
        self.label_21.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, \n"
            "stop:0 rgb(229, 153, 163), stop:1 rgb(70, 63, 125));\n"
            "border-radius: 40px;")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.button_home_2 = QtWidgets.QPushButton(self.page_lose)
        self.button_home_2.setGeometry(QtCore.QRect(130, 350, 451, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button_home_2.setFont(font)
        self.button_home_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_home_2.setStyleSheet("QPushButton#button_home_2{\n"
                                         "background-color:rgb(77, 56, 76);\n"
                                         "color: \'white\';\n"
                                         "border-radius: 7px;\n"
                                         "}\n"
                                         "QPushButton#button_home_2:hover{\n"
                                         "background-color:rgb(226, 151, 162);\n"
                                         "}\n"
                                         "QPushButton#button_home_2:pressed{\n"
                                         "padding-top:5px;\n"
                                         "padding-left:5px;\n"
                                         "}")
        self.button_home_2.setObjectName("button_home_2")
        self.label_label22 = QtWidgets.QLabel(self.page_lose)
        self.label_label22.setGeometry(QtCore.QRect(0, 110, 490, 151))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_label22.setFont(font)
        self.label_label22.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                         "color: rgb(249, 242, 232);\n"
                                         "padding: 10px")
        self.label_label22.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.label_label22.setWordWrap(True)
        self.label_label22.setObjectName("label_label22")
        self.label_label23 = QtWidgets.QLabel(self.page_lose)
        self.label_label23.setGeometry(QtCore.QRect(490, 110, 220, 80))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_label23.setFont(font)
        self.label_label23.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                         "color: rgb(249, 242, 232);\n"
                                         "padding-right: 10px;\n"
                                         "padding-bottom: 5px;")
        self.label_label23.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.label_label23.setWordWrap(True)
        self.label_label23.setObjectName("label_label23")
        self.label_score_lose = QtWidgets.QLabel(self.page_lose)
        self.label_score_lose.setGeometry(QtCore.QRect(490, 190, 220, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_score_lose.setFont(font)
        self.label_score_lose.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                            "color: rgb(249, 242, 232);\n"
                                            "padding-right: 10px;\n"
                                            "color:rgb(255, 0, 0);")
        self.label_score_lose.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)
        self.label_score_lose.setWordWrap(True)
        self.label_score_lose.setObjectName("label_score_lose")
        self.stackedWidget.addWidget(self.page_lose)
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.label_1 = QtWidgets.QLabel(self.page_home)
        self.label_1.setGeometry(QtCore.QRect(0, 0, 381, 525))
        self.label_1.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, \n"
            "stop:0 rgb(229, 153, 163), stop:1 rgb(70, 63, 125));\n"
            "border-radius: 40px;")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_8 = QtWidgets.QLabel(self.page_home)
        self.label_8.setGeometry(QtCore.QRect(200, 270, 180, 240))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(250)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(229, 153, 163);")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.page_home)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 381, 110))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                   "color: rgb(249, 242, 232);\n"
                                   "padding: 10px")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_home)
        self.label_4.setGeometry(QtCore.QRect(0, 170, 381, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                   "color: rgb(249, 242, 232);\n"
                                   "padding: 10px;")
        self.label_4.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_home)
        self.label_5.setGeometry(QtCore.QRect(210, 180, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.page_home)
        self.label_6.setGeometry(QtCore.QRect(20, 400, 70, 110))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(100)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(229, 153, 163);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.page_home)
        self.label_7.setGeometry(QtCore.QRect(110, 350, 120, 170))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(150)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(229, 153, 163);")
        self.label_7.setObjectName("label_7")
        self.label_2 = QtWidgets.QLabel(self.page_home)
        self.label_2.setGeometry(QtCore.QRect(340, 40, 371, 451))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-top-right-radius: 35px;\n"
                                   "border-bottom-right-radius: 35px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.page_dif = QtWidgets.QWidget()
        self.page_dif.setObjectName("page_dif")

        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.button_general = QtWidgets.QPushButton(self.page_home)
        self.button_general.setGeometry(QtCore.QRect(410, 80, 270, 60))
        self.button_general.setObjectName("button_general")
        self.button_nature = QtWidgets.QPushButton(self.page_home)
        self.button_nature.setGeometry(QtCore.QRect(410, 280, 270, 60))
        self.button_nature.setObjectName("button_nature")
        self.button_computer = QtWidgets.QPushButton(self.page_home)
        self.button_computer.setGeometry(QtCore.QRect(410, 180, 271, 61))
        self.button_computer.setObjectName("button_computer")
        self.button_history = QtWidgets.QPushButton(self.page_home)
        self.button_history.setGeometry(QtCore.QRect(410, 380, 271, 61))
        self.button_history.setObjectName("button_history")
        self.button_easy = QtWidgets.QPushButton(self.page_dif)
        self.button_easy.setGeometry(QtCore.QRect(410, 110, 271, 61))
        self.button_easy.setObjectName("button_easy")
        self.button_medium = QtWidgets.QPushButton(self.page_dif)
        self.button_medium.setGeometry(QtCore.QRect(410, 230, 271, 61))
        self.button_medium.setObjectName("button_medium")
        self.button_difficult = QtWidgets.QPushButton(self.page_dif)
        self.button_difficult.setGeometry(QtCore.QRect(410, 350, 271, 61))
        self.button_difficult.setObjectName("button_difficult")
        category_buttons = [self.button_computer, self.button_history, self.button_general, self.button_nature,
                            self.button_easy, self.button_medium, self.button_difficult]
        for button in category_buttons:
            button.setFont(font)
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            name = button.objectName()
            button.setStyleSheet(f"QPushButton#{name}"
                                 "{\n"
                                 "background-color: rgb(49, 40, 69);\n"
                                 "color: \'white\';\n"
                                 "border-radius: 7px;\n"
                                 "}\n"
                                 f"QPushButton#{name}:hover"
                                 "{\n"
                                 "background-color:rgb(226, 151, 162);\n"
                                 "}\n"
                                 f"QPushButton#{name}:pressed"
                                 "{\n"
                                 "padding-top:5px;\n"
                                 "padding-left:5px;\n}")

        self.label_2.raise_()
        self.label_1.raise_()
        self.label_8.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.button_general.raise_()
        self.button_nature.raise_()
        self.button_computer.raise_()
        self.button_history.raise_()
        self.stackedWidget.addWidget(self.page_home)
        self.label_13 = QtWidgets.QLabel(self.page_dif)
        self.label_13.setGeometry(QtCore.QRect(210, 180, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(22)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: white;")
        self.label_13.setObjectName("label_13")



        self.label_9 = QtWidgets.QLabel(self.page_dif)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 381, 525))
        self.label_9.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0.994, y1:1, x2:1, y2:0, stop:0 "
            "rgb(229, 153, 163), stop:1 rgb(70, 63, 125));\n"
            "border-radius: 40px;")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_dif)
        self.label_10.setGeometry(QtCore.QRect(340, 40, 371, 451))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("\n"
                                    "background-color: rgba(255, 255, 255, 255);\n"
                                    "border-top-right-radius: 35px;\n"
                                    "border-bottom-right-radius: 35px;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_14 = QtWidgets.QLabel(self.page_dif)
        self.label_14.setGeometry(QtCore.QRect(20, 400, 70, 110))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(100)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: rgb(229, 153, 163);")
        self.label_14.setObjectName("label_14")
        self.label_11 = QtWidgets.QLabel(self.page_dif)
        self.label_11.setGeometry(QtCore.QRect(0, 60, 381, 110))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                    "color: rgb(249, 242, 232);\n"
                                    "padding: 10px")
        self.label_11.setObjectName("label_11")
        self.label_16 = QtWidgets.QLabel(self.page_dif)
        self.label_16.setGeometry(QtCore.QRect(200, 270, 180, 240))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(250)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(229, 153, 163);")
        self.label_16.setObjectName("label_16")
        self.label_15 = QtWidgets.QLabel(self.page_dif)
        self.label_15.setGeometry(QtCore.QRect(110, 350, 120, 170))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(150)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(229, 153, 163);")
        self.label_15.setObjectName("label_15")

        self.label_12 = QtWidgets.QLabel(self.page_dif)
        self.label_12.setGeometry(QtCore.QRect(0, 170, 381, 50))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: rgba(0, 0, 0, 120);\n"
                                    "color: rgb(249, 242, 232);\n"
                                    "padding: 10px;")
        self.label_12.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.label_12.setObjectName("label_12")
        self.button_backdif = QtWidgets.QPushButton(self.page_dif)
        self.button_backdif.setGeometry(QtCore.QRect(380, 450, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Wingdings")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button_backdif.setFont(font)
        self.button_backdif.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_backdif.setStyleSheet("QPushButton#button_backdif{\n"
                                          "background-color:rgba(0, 0, 0, 0);\n"
                                          "color:rgb(47, 38, 66);\n"
                                          "border-radius: 7px;\n"
                                          "}\n"
                                          "QPushButton#button_backdif:hover{\n"
                                          "color:rgb(226, 151, 162);\n"
                                          "}\n"
                                          "QPushButton#button_backdif:pressed{\n"
                                          "padding-top:5px;\n"
                                          "padding-left:5px;\n"
                                          "}")
        self.button_backdif.setObjectName("button_backdif")
        self.label_10.raise_()
        self.button_easy.raise_()
        self.label_9.raise_()
        self.label_14.raise_()
        self.label_11.raise_()
        self.label_16.raise_()
        self.label_15.raise_()
        self.button_medium.raise_()
        self.button_difficult.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.button_backdif.raise_()
        self.stackedWidget.addWidget(self.page_dif)
        self.button_min = QtWidgets.QPushButton(Form)
        self.button_min.setGeometry(QtCore.QRect(760, 110, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button_min.setFont(font)
        self.button_min.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_min.setStyleSheet("QPushButton#button_min{\n"
                                      "background-color:rgb(50, 41, 69);\n"
                                      "color: \'white\';\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton#button_min:hover{\n"
                                      "background-color:rgb(226, 151, 162);\n"
                                      "}\n"
                                      "QPushButton#button_min:pressed{\n"
                                      "padding-top:3px;\n"
                                      "padding-left:3px;\n"
                                      "}")
        self.button_min.setObjectName("button_min")
        self.button_info = QtWidgets.QLabel(Form)
        self.button_info.setGeometry(QtCore.QRect(760, 140, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Harlow Solid Italic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button_info.setFont(font)
        self.button_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_info.setStyleSheet("QLabel#button_info{\n"
                                       "background-color:rgb(50, 41, 69);\n"
                                       "color: \'white\';\n"
                                       "border-radius: 5px;\n"
                                       "padding: 5px;\n"
                                       "}\n"
                                       "QLabel#button_info:hover{\n"
                                       "background-color:rgb(226, 151, 162);\n"
                                       "}")
        self.button_info.setObjectName("button_info")
        self.button_close = QtWidgets.QPushButton(Form)
        self.button_close.setGeometry(QtCore.QRect(760, 80, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Wingdings 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.button_close.setFont(font)
        self.button_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_close.setStyleSheet("QPushButton#button_close{\n"
                                        "background-color:rgb(50, 41, 69);\n"
                                        "color: \'white\';\n"
                                        "border-radius: 5px;\n"
                                        "}\n"
                                        "QPushButton#button_close:hover{\n"
                                        "background-color:rgb(226, 151, 162);\n"
                                        "}\n"
                                        "QPushButton#button_close:pressed{\n"
                                        "padding-top:3px;\n"
                                        "padding-left:3px;\n"
                                        "}")
        self.button_close.setObjectName("button_close")
        self.button_min.raise_()
        self.button_info.raise_()
        self.button_close.raise_()
        self.stackedWidget.raise_()

        self.button_close.clicked.connect(Form.close)
        self.button_min.clicked.connect(Form.showMinimized)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_question.setText(_translate("Form", "Question"))
        self.button_answer1.setText(_translate("Form", "Answer1"))
        self.button_answer4.setText(_translate("Form", "Answer4"))
        self.button_answer2.setText(_translate("Form", "Answer2"))
        self.button_answer3.setText(_translate("Form", "Answer3"))
        self.button_back.setToolTip(_translate("Form", "Back/Cancel"))
        self.button_back.setText(_translate("Form", "ç"))
        self.label_score.setText(_translate("Form", "0"))
        self.label_s.setText(_translate("Form", " Score: "))
        self.button_home.setText(_translate("Form", "Play Again"))
        self.label_19.setText(_translate("Form", "Congratulations! You won!"))
        self.label_20.setText(_translate("Form", "Your final score:"))
        self.label_score_win.setText(_translate("Form", "100"))
        self.button_home_2.setText(_translate("Form", "Play Again"))
        self.label_label22.setText(_translate("Form", "Sorry! Your score is too low..."))
        self.label_label23.setText(_translate("Form", "Your final score:"))
        self.label_score_lose.setText(_translate("Form", "50"))
        self.label_8.setText(_translate("Form", "?"))
        self.label_3.setText(_translate("Form", "Trivia Quiz"))
        self.label_4.setText(_translate("Form", "Choose Category"))
        self.label_5.setText(_translate("Form", "è"))
        self.label_6.setText(_translate("Form", "?"))
        self.label_7.setText(_translate("Form", "?"))
        self.button_general.setText(_translate("Form", "General Knowledge"))
        self.button_nature.setText(_translate("Form", "Science and Nature"))
        self.button_computer.setText(_translate("Form", "Computer Science"))
        self.button_history.setText(_translate("Form", "History"))
        self.label_13.setText(_translate("Form", "è"))
        self.button_easy.setText(_translate("Form", "Easy"))
        self.label_14.setText(_translate("Form", "?"))
        self.label_11.setText(_translate("Form", "Quizzy Quiz"))
        self.label_16.setText(_translate("Form", "?"))
        self.label_15.setText(_translate("Form", "?"))
        self.button_medium.setText(_translate("Form", "Medium"))
        self.button_difficult.setText(_translate("Form", "Hard"))
        self.label_12.setText(_translate("Form", "Choose Difficulty"))
        self.button_backdif.setToolTip(_translate("Form", "Back"))
        self.button_backdif.setText(_translate("Form", "ç"))
        self.button_min.setToolTip(_translate("Form", "Minimize"))
        self.button_min.setText(_translate("Form", "-"))
        self.button_close.setToolTip(_translate("Form", "Close"))
        self.button_close.setText(_translate("Form", "Ó"))
        self.button_info.setToolTip(_translate("Form", "<html><head/><body><p><span "
                                                       "style=' font-size:10pt;'>To play choose "
                                                       "category and difficulty. You will then get 10 "
                                                       "randomly selected questions. </span></p><p><span "
                                                       "style=' font-size:10pt;'>Get points for each correct "
                                                       "answer: first try - </span><span "
                                                       "style=' font-size:10pt; font-weight:600;'>10 points</span>"
                                                       "<span style=' font-size:10pt;'>; second try - </span><span "
                                                       "style=' font-size:10pt; font-weight:600;'>7 points</span>"
                                                       "<span style=' font-size:10pt;'>; third - </span><span "
                                                       "style=' font-size:10pt; font-weight:600;'>3 points</span>"
                                                       "<span style=' font-size:10pt;'>; fourth -</span><span "
                                                       "style=' font-size:10pt; font-weight:600;'> 0. </span></p><p>"
                                                       "<span style=' font-size:10pt;'>Score over </span><span "
                                                       "style=' font-size:10pt; font-weight:600;'>75</span><span "
                                                       "style=' font-size:10pt;'> points to</span><span "
                                                       "style=' font-size:10pt; font-weight:600;'> win</span><span "
                                                       "style=' font-size:10pt;'> the game!</span></p></body></html>"))
        self.button_info.setText(_translate("Form", "i"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
