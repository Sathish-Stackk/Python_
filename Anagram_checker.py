word1 = input("Enter first word: ").lower()
word2 = input("Enter second word: ").lower()

if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not an Anagram")
