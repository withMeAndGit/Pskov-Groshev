import sys

import random

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPaintEvent
from PyQt6.QtCore import QPointF

from main_ui import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    """
    mini PyQt6 app
    """

    def __init__(self) -> None:
        """
        init window
        """
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(800, 600)

        self.initUI()

    def initUI(self) -> None:
        self.setGeometry(300, 300,
                         1_000, 1_000)

        self.qp = QPainter()
        self.flag = False

        self.initBtn.clicked.connect(self.draw)

    def draw(self) -> None:
        """
        message to draw
        :return: None
        """

        self.flag = True
        self.update()

    def get_random_pos(self) -> tuple[int, int]:
        """
        return random position in window
        :return: tuple[int, int]
        """

        return (random.randint(0, self.width()),
                random.randint(0, self.height()))

    def get_random_color(self) -> tuple[int, int, int]:
        """
        return random color (RGB)
        :return: tuple[int, int, int]
        """

        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    def paintEvent(self, event: QPaintEvent) -> None:
        """
        draw ellipse
        :param event:   QPaintEvent
        :return:        None
        """

        if self.flag:
            self.qp.begin(self)

            size = random.randint(20, 100)
            self.qp.setBrush(QColor(*self.get_random_color()))

            self.qp.drawEllipse(QPointF(*self.get_random_pos()),
                                size, size)

            self.qp.end()
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
