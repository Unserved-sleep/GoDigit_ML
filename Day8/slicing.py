word = input()
sliced_word = word[0] + word[int(len(word)/2) - 1] + word[-1]
print(sliced_word)
