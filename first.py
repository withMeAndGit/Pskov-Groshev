import io
import sys

import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPaintEvent
from PyQt6.QtCore import QPointF

with open('UI.ui', 'r', encoding='utf-8') as ui:
    template = ''.join(map(lambda ln: ln.strip(), ui.readlines().copy()))


class Main(QMainWindow):
    """
    mini PyQt6 app
    """

    def __init__(self) -> None:
        """
        init window
        """
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)

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

    def paintEvent(self, event: QPaintEvent) -> None:
        """
        draw ellipse
        :param event:   QPaintEvent
        :return:        None
        """

        if self.flag:
            self.qp.begin(self)

            size = random.randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))

            self.qp.drawEllipse(QPointF(*self.get_random_pos()),
                                size, size)

            self.qp.end()
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
