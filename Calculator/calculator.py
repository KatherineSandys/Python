import PyQt5.QtWidgets as qtw
from PyQt5 import QtCore, QtGui
import PyQt5.QtGui
import PyQt5.QtCore

import sys


class Window(qtw.QMainWindow):

    def __init__(self):
        super().__init__()
        # setting title
        self.setWindowTitle("Python ")
        
        self.setGeometry(100, 100, 360, 350)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()

    def UiComponents(self):
        # creating a label
        self.label = qtw.QLabel(self)
        self.label.setGeometry(5, 5, 350, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")                                 
        # setting font
        self.label.setFont(PyQt5.QtGui.QFont('Arial', 15))
        # adding number button to the screen
        
        push1 = qtw.QPushButton("1", self)        
        push1.setGeometry(5, 150, 80, 40)
        
        push2 = qtw.QPushButton("2", self)        
        push2.setGeometry(95, 150, 80, 40)
        
        push3 = qtw.QPushButton("3", self)        
        push3.setGeometry(185, 150, 80, 40)
        
        push4 = qtw.QPushButton("4", self)        
        push4.setGeometry(5, 200, 80, 40)
        
        push5 = qtw.QPushButton("5", self)        
        push5.setGeometry(95, 200, 80, 40)
        
        push6 = qtw.QPushButton("5", self)        
        push6.setGeometry(185, 200, 80, 40)
        
        push7 = qtw.QPushButton("7", self)        
        push7.setGeometry(5, 250, 80, 40)
        
        push8 = qtw.QPushButton("8", self)        
        push8.setGeometry(95, 250, 80, 40)
        
        push9 = qtw.QPushButton("9", self)        
        push9.setGeometry(185, 250, 80, 40)
        
        push0 = qtw.QPushButton("0", self)        
        push0.setGeometry(5, 300, 80, 40)

        push_equal = qtw.QPushButton("=", self)        
        push_equal.setGeometry(275, 300, 80, 40)
        # adding equal button a color effect
        c_effect = qtw.QGraphicsColorizeEffect()
        push_equal.setGraphicsEffect(c_effect)

        push_plus = qtw.QPushButton("+", self)        
        push_plus.setGeometry(275, 250, 80, 40)
         
        push_minus = qtw.QPushButton("-", self)        
        push_minus.setGeometry(275, 200, 80, 40)
         
        push_mul = qtw.QPushButton("*", self)        
        push_mul.setGeometry(275, 150, 80, 40)
         
        push_div = qtw.QPushButton("/", self)        
        push_div.setGeometry(185, 300, 80, 40)
         
        push_point = qtw.QPushButton(".", self)        
        push_point.setGeometry(95, 300, 80, 40)

        # clear button
        push_clear = qtw.QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 200, 40)

        # del one character button
        push_del = qtw.QPushButton("Del", self)
        push_del.setGeometry(210, 100, 145, 40)

        # adding action to each of the button
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.button_zero)
        push1.clicked.connect(self.button_one)
        push2.clicked.connect(self.button_two)
        push3.clicked.connect(self.button_three)
        push4.clicked.connect(self.button_four)
        push5.clicked.connect(self.button_five)
        push6.clicked.connect(self.button_six)
        push7.clicked.connect(self.button_seven)
        push8.clicked.connect(self.button_eight)
        push9.clicked.connect(self.button_nine)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)

    def action_equal(self):

        # get the label text
        equation = self.label.text()
        try:
            # getting the ans
            ans = eval(equation)
            # setting text to the label
            self.label.setText(str(ans))
        except:
            # setting text to the label
            self.label.setText("Wrong Input")

    def action_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")

    def button_zero(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")

    def button_one(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")

    def button_two(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")

    def button_three(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")

    def button_four(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")

    def button_five(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")

    def button_six(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")

    def button_seven(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")

    def button_eight(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")

    def button_nine(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        # clearing the label text
        self.label.setText("")

    def action_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])


# create pyqt5 app
App = qtw.QApplication(sys.argv)
# create the instance of our Window
window = Window()
# start
sys.exit(App.exec())
