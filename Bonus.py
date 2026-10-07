sentence = "I am a big fan of Al Ittihad club and I really love Al Ittihad"
word = "Ittihad"

print("Length of sentence:", len(sentence))
print("Index of the word:", sentence.find(word))
print("Word count:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("After replacement:", sentence.replace(word, "Champions"))
print("Last character:", sentence[-1])