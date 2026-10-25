squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares)

words = ["apple", "banana", "cherry"]
lengths = {w: len(w) for w in words}
print(lengths)

print(sorted(set("banana")))
