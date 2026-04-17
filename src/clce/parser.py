from lark import Lark

class CLCEParser:
    def __init__(self):
        self.parser = Lark(r'''
            start: sentence "."

            sentence: quantifier term "is" "on" "a" term
                    | "The" term name "sees" "the" term name "in" "the" "building" building_name
                    | "Nothing" "is" "an" "element" "of" "the" "set" name
                    | name "is" "a" relational "of" name
                    | "Declare" quoted "as" "name" "of" noun

            quantifier: "Every" | "The" | "A" | "An"
            term: WORD
            name: WORD
            relational: WORD
            noun: WORD
            building_name: WORD+
            quoted: "'" WORD "'" | "'" WORD "''" WORD "'"

            WORD: /[a-zA-Z0-9_]+/
            %ignore " "
            %ignore /\s+/
        ''', start='start')

    def parse(self, text):
        return self.parser.parse(text)

    def pretty(self, tree):
        return tree.pretty()
