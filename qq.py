from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from descr import *
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

app=QApplication([])
mw=MainWin()
app.exec_()
























app=QApplication([])
app.exec_()