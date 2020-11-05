import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout
)

from color_widget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Nested Layout Demo")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('green'))
        layout2.addWidget(Color('blue'))

        layout1.addLayout(layout2)

        layout1.addWidget(Color('pink'))

        layout3.addWidget(Color('purple'))
        layout3.addWidget(Color('orange'))

        layout1.addLayout(layout3)

        # In order to add a layout to a QMainWindow, we need to add the layout to a dummy widget.
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
