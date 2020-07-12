'''main_window.py'''
from libs.content import UlanjiContent
from libs.renderer import UlanjiRenderer
from PyQt5 import uic
from PyQt5.QtWidgets import qApp, QAction, QFileDialog, QHBoxLayout, QLabel, QMainWindow, QSizePolicy, QSplitter
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QUrl, QObject, pyqtSlot
import os

class MainWindow(QMainWindow):
    '''
    Main Window class inherited from QMainWindow

    Args:
        args (list): optional variable length argument list
        kwargs (list): optional keyword argument list
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ulanji = UlanjiContent()
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.ui = uic.loadUi(f"{current_path}/main_window.ui", self)
        self.init_menubar_actions()
        self.init_menubar_shortcuts()
        self.init_statusbar()
        self.ui.editorPane.textChanged.connect(self.editor_pane_updated)
        self.channel = QWebChannel()
        self.renderer = UlanjiRenderer()
        self.channel.registerObject("backend", self.renderer)
        self.ui.rendererPane.page().setWebChannel(self.channel)
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../assets/renderer.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.ui.rendererPane.load(local_url)

    def init_menubar_actions(self):
        '''
        Initialize menu bar action handler
        '''
        self.ui.menubar.triggered[QAction].connect(self.menubar_action_handler)

    def init_menubar_shortcuts(self):
        '''
        Initialize menu bar button shortcuts
        '''
        self.ui.actionNew.setShortcut("Ctrl+N")
        self.ui.actionOpen.setShortcut("Ctrl+O")
        self.ui.actionSave.setShortcut("Ctrl+S")
        self.ui.actionSave_As.setShortcut("Ctrl+Shift+S")
        self.ui.actionExit.setShortcut("Ctrl+Q")

    def init_statusbar(self):
        '''
        Initialize status bar widgets and components
        '''
        self.ui.statusbarFileNameLabel = QLabel('file:')
        self.ui.statusbarFileNameValue = QLabel('')
        self.statusBar().addPermanentWidget(self.ui.statusbarFileNameLabel)
        self.statusBar().addPermanentWidget(self.ui.statusbarFileNameValue)

        self.ui.statusbarWordCountLabel = QLabel('\twords:')
        self.ui.statusbarWordCountValue = QLabel('0')
        self.statusBar().addPermanentWidget(self.ui.statusbarWordCountLabel)
        self.statusBar().addPermanentWidget(self.ui.statusbarWordCountValue)

        self.ui.statusbarCharCountLabel = QLabel('\tchars:')
        self.ui.statusbarCharCountValue = QLabel('0')
        self.statusBar().addPermanentWidget(self.ui.statusbarCharCountLabel)
        self.statusBar().addPermanentWidget(self.ui.statusbarCharCountValue)

    def editor_pane_updated(self):
        self.ulanji.update_content(self.ui.editorPane.toPlainText())
        self.renderer.set_content(self.ui.editorPane.toPlainText())
        self.ui.rendererPane.reload()
        self.statusbar_update_values()

    def menubar_action_handler(self, action):
        '''
        Menu bar action handler
        '''
        try:
            getattr(
                self, f'menubar_action_{action.text().lower().strip("1&")}')()
        except AttributeError as error:
            print(error)

    def menubar_action_exit(self):
        '''
        Menu bar action: exit file
        '''
        # TODO: check if current content is edited
        qApp.quit()

    def menubar_action_new(self):
        '''
        Menu bar action: create new file
        '''
        # TODO: add check if current content is edited
        # TODO: add open new file

    def menubar_action_open(self):
        '''
        Menu bar action: open file
        '''
        # TODO: check if current content is edited and ask save
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Open file",
            "",
            "All Files (*)",
            options=options
        )

        if file_path:
            self.ulanji.set_content(file_path)
            self.ui.editorPane.setPlainText(self.ulanji.content)
            self.statusbar_update_values()

    def menubar_action_save(self):
        '''
        Menu bar action: save file
        '''
        # TODO: check if currrent content has file name

    def menubar_action_save_as(self):
        '''
        Menu bar action: save_as file
        '''
        # TODO: check if current content is edited

    def statusbar_update_values(self):
        '''
        Update status bar values on change content
        '''
        self.ui.statusbarFileNameValue.setText(self.ulanji.file_name)
        self.ui.statusbarWordCountValue.setText(str(self.ulanji.word_count))
        self.ui.statusbarCharCountValue.setText(str(self.ulanji.char_count))
