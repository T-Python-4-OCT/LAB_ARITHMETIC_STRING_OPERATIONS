sentence = "Barcelona is my favorite team and I watch every Barcelona match with my friends"
word = "Barcelona"

print(len(sentence))
print(sentence.find(word))
print(sentence.count(word))
print(sentence.upper())
print(sentence.lower())
new_sentence = sentence.replace(word, "Barca")
print(new_sentence)
print(sentence[-1])
