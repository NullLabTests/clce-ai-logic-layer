from src.clce.parser import CLCEParser
from src.clce.translator import CLCEToFOL

print("=== CLCE v1.1 ===")
print("Parser + Real FOL Translator\n")

parser = CLCEParser()
translator = CLCEToFOL()

examples = [
    "Every cat is on a mat.",
    "The woman Sue sees the cat Yojo in the building Grand Central Terminal.",
    "Nothing is an element of the set empty_set.",
    "Bob is a child of Sue.",
    "Declare Grand Central Terminal as name of building.",
    "Declare 'Grand Central Terminal' as name of building."
]

for s in examples:
    print("CLCE:", s)
    tree = parser.parse(s)
    print("AST OK")
    fol = translator.to_fol(tree)
    print("FOL:", fol)
    print("---")
