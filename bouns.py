sentence:str = "fahad learn programming language python she is esey language and powerfol language"
word:str = "python"

print("Length:", len(sentence))
print("Index:", sentence.index(word))
print("Count:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
new_sentence = sentence.replace(word, "c++")
print("Replaced:", new_sentence)
print("Last character:", sentence[-1])