from src.clce.parser import CLCEParser

print("=== CLCE AI Logic Layer v0.4 ===")
print("Better parser based on Sowa 2004\n")

parser = CLCEParser()

examples = [
    "Every cat is on a mat.",
    "The woman Sue sees the cat Yojo in the building Grand Central Terminal.",
    "Nothing is an element of the set empty_set.",
    "Bob is a child of Sue.",
    "Declare Grand Central Terminal as name of building."
]

for s in examples:
    print("CLCE:", s)
    try:
        tree = parser.parse(s)
        print("OK")
        print(parser.pretty(tree))
    except Exception as e:
        print("ERROR:", str(e)[:100])
    print("---")
