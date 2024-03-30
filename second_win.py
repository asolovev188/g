from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    def initUI(self):
        self.pupu=QLabel('Введите ФИО:')
        self.okoshko1=QLineEdit(' ')
        self.dududu=QLabel("Полных лет:")
        self.okoshko2=QLineEdit(' ')
        self.kukuku=QLabel("Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку,чтобы запустить тест. Результат запишите в соответствующие поле")
        self.okoshko3=QLineEdit(' ')
        self.tututu=QPushButton('txt_next',self)
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.pupu,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.okoshko1,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.dududu,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.okoshko2,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.kukuku,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.tututu,alignment=Qt.AlignLeft)
        self.layout_line.addWidget(self.okoshko3,alignment=Qt.AlignLeft)
        self.setLayout(self.layout_line)
app=QApplication([])
mw=TestWin()
app.exec_()