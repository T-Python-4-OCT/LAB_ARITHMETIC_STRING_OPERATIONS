sentence = "I love learning Python because programing is fun and useful"
word = "Python"
print("Length:", len(sentence))
print("First index:", sentence.index(word))
print("Count:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
new_sentence = sentence.replace(word, "java")
print("New sentence:", new_sentence)
print("Last charachter:", sentence[-1])
