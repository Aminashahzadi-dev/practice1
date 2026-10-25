sentence = "the cat and the hat and the bat"
words = sentence.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)

top = max(freq, key=freq.get)
print("Sab se common:", top, freq[top])
