sentence = "Python is useful, and Python make programming easier"
word = "Python"

print("Sentence length:", len(sentence))
print("First occurrence index:", sentence.find(word))
print("Word count:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Replaced sentence:", sentence.replace(word, "Coding"))
print("Last character:", sentence[-1])