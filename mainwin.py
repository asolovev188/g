
from PyQt5.QtCore import Qt, QTimer, QTime,QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import*
from math import*
#from descr import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.d=QPushButton('Дескриминант',self)
        self.slozhenie=QPushButton('Сложение',self)
        self.vichitanie=QPushButton('Вычитание',self)
        self.layout_line=QHBoxLayout()
        self.layout_line.addWidget(self.d,alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.slozhenie,alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.vichitanie,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click1(self):
        self.tw=DESCR()
        self.hide()    
    def connects(self):
        self.d.clicked.connect(self.next_click1)
    
    def set_appear(self):
        win_x, win_y =200,100
        win_width,win_height=1000,600
        self.setWindowTitle('Решение математических задач')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
class DESCR(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.formula1=QLabel('ax^2+bx+c=0')
        self.formula2=QLabel('D=b^2-4ac')
        self.a=QLineEdit('')
        self.b=QLineEdit('')
        self.c=QLineEdit('')
        self.otvet1=QPushButton('рассчитать все ответы:')
        self.otvet4=QLabel("рассчитанный ответ D:")
        self.show1=QLabel('дискриминант:')
        self.otvet2=QLabel('рассчитанный ответ x1:')
        self.show2=QLabel('x1:')
        self.otvet3=QLabel('рассчитанный ответ x2:')
        self.show3=QLabel('x2:')
        self.back1=QPushButton('главное меню')
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.formula1,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.formula2,alignment=Qt.AlignLeft)
        self.layout_line2=QHBoxLayout()   
        self.layout_line2.addWidget(self.a,alignment=Qt.AlignCenter)
        self.layout_line2.addWidget(self.b,alignment=Qt.AlignCenter)
        self.layout_line2.addWidget(self.c,alignment=Qt.AlignCenter)
        self.layout_line.addLayout(self.layout_line2)
        self.layout_line.addWidget(self.otvet1,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.otvet4,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.show1,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.otvet2,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.show2,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.otvet3,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.show3,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.back1,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)

        
        self.validator=QDoubleValidator()
        self.loc=QLocale(QLocale.English,QLocale.UnitedStates)
        self.validator.setLocale(self.loc)
        self.a.setValidator(self.validator)
        self.a.setValidator(QIntValidator(-2147483648,2147483647))
        self.b.setValidator(self.validator)
        self.b.setValidator(QIntValidator(-2147483648,2147483647))
        self.c.setValidator(self.validator)
        self.c.setValidator(QIntValidator(-2147483648,2147483647))

    def next_click2(self):
        self.tw=MainWin()
        self.hide()
    def otvet_descr(self):
        otvet_a=int(self.a.text())
        otvet_b=int(self.b.text())
        otvet_c=int(self.c.text())
        ok1=otvet_a*otvet_a-4*otvet_b*otvet_c
        self.show1.setText(str(ok1))
        x1=((-otvet_b+sqrt(ok1))/(2*otvet_a))
        self.show2.setText(str(x1))
        x2=((-otvet_b-sqrt(ok1))/(2*otvet_a))
        self.show3.setText(str(x2))

    


    def connects(self):
        self.back1.clicked.connect(self.next_click2)
        self.otvet1.clicked.connect(self.otvet_descr)
    def set_appear(self):
        win_x, win_y =200,100
        win_width,win_height=1000,600
        self.setWindowTitle('Дескриминант')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

app=QApplication([])
mw=MainWin()
app.exec_()
























app=QApplication([])
app.exec_()