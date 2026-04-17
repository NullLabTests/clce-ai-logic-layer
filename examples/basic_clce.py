from src.clce.parser import CLCEParser

print("=== CLCE AI Logic Layer v0.2 ===")
print("Based on John F. Sowa 2004\n")

parser = CLCEParser()

sentences = [
    "Every cat is on a mat.",
    "Some person is between a rock and a hard place.",
    "Every prime number is a number."
]

for s in sentences:
    print("Sentence:", s)
    tree = parser.parse(s)
    print("Status: ✅ Parsed successfully")
    print("Tree:")
    print(parser.pretty(tree))
    print("-" * 50)
