'''
main.py

This module acts as the entrypoint for the entire application

Attributes:
    app (QApplication): pyqt5 application instance

    window (MainWindow): window class invoked to render the ui
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets, uic
from ulanji.gui.main_window import MainWindow


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
