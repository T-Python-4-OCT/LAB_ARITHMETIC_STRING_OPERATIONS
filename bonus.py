# جملة تحتوي على أكثر من 10 كلمات.
sentence = (
    "Python makes learning strings fun, and Python helps beginners "
    "practice useful coding skills every day."
)
# الكلمة التي سنبحث عنها داخل الجملة.
word = "Python"

# طباعة عدد أحرف الجملة، ثم أول موقع للكلمة وعدد مرات تكرارها.
print(f"Sentence length: {len(sentence)}")
print(f"First occurrence of '{word}': index {sentence.find(word)}")
print(f"Occurrences of '{word}': {sentence.count(word)}")

# طباعة الجملة مرة بحروف كبيرة ومرة بحروف صغيرة.
print(f"Uppercase: {sentence.upper()}")
print(f"Lowercase: {sentence.lower()}")

# استبدال كل ظهور للكلمة بكلمة جديدة، ثم طباعة آخر حرف من الجملة الناتجة.
updated_sentence = sentence.replace(word, "Coding")
print(f"Sentence with replacement: {updated_sentence}")
print(f"Last character: {updated_sentence[-2]}")
