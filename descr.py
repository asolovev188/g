from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from mainwin import*
class DESCR(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.formula=QLabel('D=b^2-4ac')
        self.a=QLineEdit('')
        self.b=QLineEdit('')
        self.c=QLineEdit('')
        self.otvet1=QPushButton('рассчитать ответ')
        self.back1=QPushButton('главное меню')
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.formula,alignment=Qt.AlignLeft)
        self.layout_line2=QHBoxLayout()   
        self.layout_line2.addWidget(self.a,alignment=Qt.AlignCenter)
        self.layout_line2.addWidget(self.b,alignment=Qt.AlignCenter)
        self.layout_line2.addWidget(self.c,alignment=Qt.AlignCenter)
        self.layout_line.addLayout(self.layout_line2)
        self.layout_line.addWidget(self.otvet1,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.back1,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    
    def next_click2(self):
        self.tw=MainWin()
        self.hide()
    def otvet_descr(self):
        otvet_a=int(self.a.text())
        otvet_b=int(self.b.text())
        otvet_b=int(self.c.text())


    def connects(self):
        self.back1.clicked.connect(self.next_click2)
        self.otvet1.clicked.connect(self.otvet_descr)
    def set_appear(self):
        win_x, win_y =200,100
        win_width,win_height=1000,600
        self.setWindowTitle('Дескриминант')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)