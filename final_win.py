from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
        self.set_appear()
    def initUI(self):
        self.n=QLabel('Индекс Руфье:')
        self.m=QLabel("Работоспособность сердца:")
        self.layout_line=QVBoxLayout()
        self.layout_line.addWidget(self.n,alignment=Qt.AlignCenter)
        self.layout_line.addWidget(self.m,alignment=Qt.AlignCenter)
        self.setLayout(self.layout_line)
    def set_appear(self):
        win_x, win_y =200,100
        win_width,win_height=1000,600
        self.setWindowTitle('Здоровье')
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
