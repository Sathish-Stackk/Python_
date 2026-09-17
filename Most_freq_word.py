text = input("Enter a sentence: ").lower()
words = text.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

most = max(frequency, key=frequency.get)

print("Most frequent word:", most)
print("Frequency:", frequency[most])
