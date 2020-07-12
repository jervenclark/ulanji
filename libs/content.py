'''libs/ulanji_content.py'''
from dataclasses import dataclass


@dataclass
class UlanjiContent:
    '''
    Content class to handle content operation

    Properties:
        content (str): string content
        char_count (int): total content character count
        file_name (str): path to currently opened file
        is_edited (bool): if the content is modified since last saved
        word_count (int): total content word count
    '''

    content: str = ''
    char_count: int = 0
    file_name: str = ''
    is_edited: bool = False
    word_count: int = 0

    def __init__(self):
        pass

    def calculate_word_count(self):
        '''
        Calculate word count from content
        '''
        self.word_count = len(self.content.split(' '))

    def calculate_char_count(self):
        '''
        Calculate character count from content
        '''
        self.char_count = self.content.count('')

    def set_content(self, file_path: str = ''):
        '''
        Set content from file
        '''
        try:
            with open(file_path, 'r') as file:
                self.file_name = file_path.split('/')[-1]
                self.file_path = file_path
                content = "".join(file.readlines())
                self.update_content(content)
        except IOError as error:
            print(error)

    def update_content(self, content: str = ''):
        '''
        Update content and recalculate counts
        '''
        self.content = content
        self.calculate_word_count()
        self.calculate_char_count()
