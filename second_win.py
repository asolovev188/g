from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from final_win import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.connects()
        self.set_appear()
    def initUI(self):
        self.pupu=QLabel('Введите ФИО:')
        self.okoshko1=QLineEdit(' ')
        self.dududu=QLabel("Полных лет:")
        self.okoshko2=QLineEdit(' ')
        self.kukuku=QLabel("Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку,чтобы запустить тест. Результат запишите в соответствующие поле")
        self.okoshko3=QLineEdit(' ')
        self.tututu=QPushButton('Начать первый тест',self)
        self.j=QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счётчик приседаний.')
        self.b=QPushButton('Начать делать приседания',self)
        self.a=QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.c=QPushButton('Начать финальный тест',self)
        self.okoshko4=QLineEdit(' ')
        self.okoshko5=QLineEdit(' ')
        self.h=QLabel('timer')
        self.k=QPushButton('Отправить результаты',self)
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.pupu,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.okoshko1,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.dududu,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.okoshko2,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.kukuku,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.tututu,alignment=Qt.AlignLeft)
        self.layout_line2=QHBoxLayout()        
        self.layout_line2.addWidget(self.okoshko3,alignment=Qt.AlignLeft)
        self.layout_line2.addWidget(self.h,alignment=Qt.AlignRight)
        self.layout_line.addLayout(self.layout_line2)
        self.layout_line.addWidget(self.j,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.b,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.a,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.c,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.okoshko4,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.okoshko5,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.k,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click2(self):
        self.tw=FinalWin()
        self.hide()
    def connects(self):
        self.k.clicked.connect(self.next_click2)
    def set_appear(self):
        win_x, win_y =200,100
        win_width,win_height=1000,600
        self.setWindowTitle('Здоровье')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
