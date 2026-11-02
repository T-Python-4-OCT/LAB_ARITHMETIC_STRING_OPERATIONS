sentence = "Gamers enjoy playing competitive online video games with their friends"
word = "Gamers"
print("Length of the sentence:", len(sentence))
print("Index of the word:", sentence.find(word))
print("Word count:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
new_word = "players"
replaced_sentence = sentence.replace(word, new_word)
print("Replaced sentence:", replaced_sentence)
print("Last character:", sentence[-1])