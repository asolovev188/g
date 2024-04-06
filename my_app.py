from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from second_win import *
class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    def initUI(self):
        self.btn_next=QPushButton('Начать',self)
        self.hello_text=QLabel('Добро пожаловать в программу по определению состояния здоровья!')
        self.instruction=QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лёжа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.hello_text,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.instruction,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.btn_next,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def next_click1(self):
        self.tw=TestWin()
        self.hide()
    def connects(self):
        self.btn_next.clicked.connect(self.next_click1)
    def set_appear(self):
        win_x, win_y =200,100
        win_width,win_height=1000,600
        self.setWindowTitle('Здоровье')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
app=QApplication([])
mw=MainWin()
app.exec_()