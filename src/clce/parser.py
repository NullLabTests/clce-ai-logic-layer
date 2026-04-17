from lark import Lark

class CLCEParser:
    def __init__(self):
        # Improved grammar based on Sowa CLCE rules
        self.parser = Lark('''
            start: sentence "."
            sentence: quantifier term verb phrase
            quantifier: "Every" | "Some" | "A" | "An"
            term: WORD
            verb: "is" | "has"
            phrase: "on" "a" term | "a" term
            
            WORD: /[a-zA-Z]+/
            %ignore " "
        ''', start='start')

    def parse(self, text: str):
        """Parse CLCE sentence"""
        return self.parser.parse(text)

    def pretty(self, tree):
        return tree.pretty()
