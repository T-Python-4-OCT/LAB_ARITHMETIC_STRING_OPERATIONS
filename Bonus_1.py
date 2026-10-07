sentence = "Python is a very easy programming language and I enjoy learning it"
word = "Python"
print(len(sentence))
print(sentence.index(word))
print(sentence.count(word))
print(sentence.upper())
print(sentence.lower())
new_sentence = sentence.replace(word, "Java")
print(new_sentence)
print(sentence[-1])