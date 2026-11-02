
sentence = "I love drawing and web development, and I try to combine art with creative website design"

word = "drawing"


print("Length:", len(sentence))


print("First index:", sentence.index(word))

print("Word count:", sentence.count(word))

 
print("Uppercase:", sentence.upper())

print("Lowercase:", sentence.lower())


new_sentence = sentence.replace(word, "Django")
print("Replaced:", new_sentence)

print("Last character:", sentence[-1])