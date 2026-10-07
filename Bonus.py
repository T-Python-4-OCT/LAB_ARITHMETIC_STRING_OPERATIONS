sentence = "I am Sami Fahad, and I love programming and playing football"

bouns = "playing"

print(len(sentence))
print(sentence.index(bouns))
print(sentence.count(bouns))
print(sentence.upper())
print(sentence.lower())

new_bouns= sentence.replace(bouns ,"not playing")
print(new_bouns)
print(sentence[-1])