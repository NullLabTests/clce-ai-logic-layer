from lark import Lark
class CLCEParser:
    def __init__(self):
        self.parser = Lark('start: sentence', start='start')
    def parse(self, text):
        return self.parser.parse(text)
