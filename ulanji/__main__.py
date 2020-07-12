'''
main.py

This module acts as the entrypoint for the entire application

Attributes:
    app (QApplication): pyqt5 application instance

    window (MainWindow): window class invoked to render the ui
'''
import sys
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, uic
from gui.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()

    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
