text = "the cat sat on the mat the cat sat"

words = text.split(" ")
freq = {}
for word in words:
    freq[word] = freq.get(word, 0)+1

top_words = list(freq.items())
for i in range (0, len(top_words)-1):
    for j in range (i+1, len(top_words)):
        if top_words[i][1] < top_words[j][1]:
            temp1, temp2 = top_words[i][0], top_words[i][1]
            top_words[i][0], top_words[i][1] = top_words[j][0], top_words[j][1]
            top_words[j][0], top_words[j][1] = temp1, temp2

print(top_words[:3])
print(len(top_words))