from markdown2 import markdown
from PyQt5.QtCore import QObject, pyqtSlot


class UlanjiRenderer(QObject):

    content = ''

    def __init__(self):
        super().__init__()
        self.markdown_extras = [
            'code-friendly',
            'code-color',
            'fenced-code-blocks',
            'footnotes',
            'header-ids',
            'tables'
        ]

    @pyqtSlot(result=str)
    def getStr(self):
        return self.content

    @pyqtSlot(str)
    def printStr(self, content):
        print(content)

    def set_content(self, content):
        self.content = markdown(content, extras=self.markdown_extras)
