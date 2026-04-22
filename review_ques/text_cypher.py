message = "hello world"
shift   = 3
encoded_word = []
char_map = {" ":" "}
for i in message:
    if i in char_map:
        encoded_word.append(char_map[i])
    else:
        char_map[i] = char_map.get(i, chr(ord(i) + shift if ord(i) < 120 else ord(i) + shift - 26))
        encoded_word.append(char_map[i])

print(message)
print("".join(encoded_word))
print(char_map)