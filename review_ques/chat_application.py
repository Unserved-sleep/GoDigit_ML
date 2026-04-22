#logs = "alice:hi bob:hello alice:how_are_you bob:good charlie:hey"
logs = input()
chat_list = list(logs.split(" "))
user_map = {}
for users in chat_list:
    temp = users.split(":")
    user_map[temp[0]] = user_map.get(temp[0], 0)+1

for users, texts in user_map.items():
    if texts > 1:
        print(users)
