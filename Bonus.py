sentence = "I am Abdulrahman and I love learning programming and improving my skills every day"

word = "learning"

print("Sentence length:", len(sentence))
print("First index of word:", sentence.find(word))
print("Word count:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("New sentence:", sentence.replace(word, "studying"))
print("Last character:", sentence[-1])