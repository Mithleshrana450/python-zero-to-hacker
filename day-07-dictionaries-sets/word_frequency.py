text = input("Enter a sentence: ")

words = text.split()
count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

sorted_words = sorted(count.items(), key=lambda x: x[1], reverse=True)

for word, freq in sorted_words:
    print(word, "->", freq)