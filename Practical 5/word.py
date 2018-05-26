unique_words = {}
text = input("Text: ")
words = text.split()

for word in words:
    frequency = unique_words.get(word, 0)
    unique_words[word] = frequency + 1

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))

words = list(unique_words.keys())
words.sort()



