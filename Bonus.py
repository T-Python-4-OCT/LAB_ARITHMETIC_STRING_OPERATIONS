sentence = "I love Python because Python is easy to learn and fun to use"
word = "Python"

print("Length:", len(sentence))

print("First index:", sentence.find(word))

print("Count:", sentence.count(word))

print("Uppercase:", sentence.upper())

print("Lowercase:", sentence.lower())

sentence = sentence.replace(word, "Java")

print("Updated sentence:", sentence)

print("Last character:", sentence[-1])