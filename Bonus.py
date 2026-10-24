sentence, word = "Today I learn great things about python thanks to my teacher in python camp" , "python"


print("Length:", len(sentence))
print("First occurrence index:", sentence.find(word))
print("Number of times the word appears:", sentence.count(word))
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("With replacement:", sentence.replace(word, "github"))
print("Last character:", sentence[-1])