sentence= "Hi my name is faris i am 20 years old , i live in makkah"
word="makkah"


print("length of the sentence: ",len(sentence))
print("index of the first word : ",sentence.find(word))
print("number of times the word :" ,sentence.count(word))
print("all uppercase letters :",sentence.upper())
print("all lowercase letters :",sentence.lower())
print(sentence.replace("faris","mohamed"))
print("the last character of the sentence: ",sentence[-1])