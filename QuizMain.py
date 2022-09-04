from PyQt5 import QtCore, QtWidgets
import sys
from frontend import Ui_Form
import random
from urllib.request import urlopen
import json
from links import links
import html

# Scaling Code
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
QtWidgets.QApplication.setHighDpiScaleFactorRoundingPolicy(QtCore.Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)


class MyWin(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dragPos = QtCore.QPoint()
        list_for_back = [self.ui.button_backdif, self.ui.button_back, self.ui.button_home, self.ui.button_home_2]
        for button in list_for_back:
            button.clicked.connect(self.back_to_home)
        self.ui.button_computer.clicked.connect(lambda: self.category_choice('computer'))
        self.ui.button_general.clicked.connect(lambda: self.category_choice('general'))
        self.ui.button_nature.clicked.connect(lambda: self.category_choice('nature'))
        self.ui.button_history.clicked.connect(lambda: self.category_choice('history'))
        self.ui.button_easy.clicked.connect(lambda: self.difficulty_choice('easy'))
        self.ui.button_medium.clicked.connect(lambda: self.difficulty_choice('medium'))
        self.ui.button_difficult.clicked.connect(lambda: self.difficulty_choice('difficult'))
        self.ui.button_answer1.released.connect(lambda: self.is_correct(self.ui.button_answer1))
        self.ui.button_answer2.released.connect(lambda: self.is_correct(self.ui.button_answer2))
        self.ui.button_answer3.released.connect(lambda: self.is_correct(self.ui.button_answer3))
        self.ui.button_answer4.released.connect(lambda: self.is_correct(self.ui.button_answer4))

    def back_to_home(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def category_choice(self, category):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.category_chosen = category

    def difficulty_choice(self, difficulty):
        self.difficulty_chosen = difficulty
        self.start_game()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def start_game(self):
        self.incorrect = 0
        self.score = 0
        self.number = 1
        self.indexes = random.sample(range(0, 30), 10)
        self.ui.label_score.setText(str(self.score))
        with urlopen(links[self.category_chosen][self.difficulty_chosen]) as webpage:
            self.data = json.loads(webpage.read().decode())['results']
        self.preload_data()
        self.ui.stackedWidget.setCurrentIndex(0)

    @staticmethod
    def split(s):
        lst = s.split(' ')
        lst.insert(len(lst) // 2, '\n')
        return ' '.join(lst)

    def preload_data(self):
        idx = random.choice(self.indexes)
        self.indexes.remove(idx)
        question = html.unescape(self.data[idx]['question'])
        self.correct = html.unescape(self.data[idx]['correct_answer'])
        if len(self.correct) > 40:
            self.correct = self.split(self.correct)
        wrong = [html.unescape(answer) for answer in self.data[idx]['incorrect_answers']]
        wrong = [self.split(answer) if len(answer) > 40 else answer for answer in wrong]
        all_answers = [self.correct] + wrong

        random.shuffle(all_answers)
        self.ui.label_question.setText(str(self.number) + '. ' + question)
        self.ui.button_answer1.setText(all_answers[0])
        self.ui.button_answer1.setEnabled(True)
        self.ui.button_answer2.setText(all_answers[1])
        self.ui.button_answer2.setEnabled(True)
        self.ui.button_answer3.setText(all_answers[2])
        self.ui.button_answer3.setEnabled(True)
        self.ui.button_answer4.setText(all_answers[3])
        self.ui.button_answer4.setEnabled(True)

    def is_correct(self, btn):
        if btn.text() == self.correct:
            if self.incorrect == 0:
                self.score += 10
            elif self.incorrect == 1:
                self.score += 7
            elif self.incorrect == 2:
                self.score += 3
            self.incorrect = 0
            self.number += 1
            if len(self.indexes) == 0:
                if self.score >= 75:
                    self.ui.stackedWidget.setCurrentIndex(1)
                    self.ui.label_score_win.setText(str(self.score))
                else:
                    self.ui.stackedWidget.setCurrentIndex(2)
                    self.ui.label_score_lose.setText(str(self.score))
            else:
                self.preload_data()
                self.ui.label_score.setText(str(self.score))
        else:
            btn.setEnabled(False)
            self.incorrect += 1


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
    centerPts = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
    y = w.ui.stackedWidget.size().height() // 2
    x = w.ui.stackedWidget.size().width() // 2
    w.showMaximized()
    w.move(centerPts.x() - x, centerPts.y() - int(y * 1.1))
    sys.exit(app.exec_())
