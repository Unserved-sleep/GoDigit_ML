from collections import UserList
from collections import UserString

#my_list = [11, 22, 33, 44, 55]
#user_list = UserList(my_list)
#print(user_list)

"""
class user_list(UserList):
    def append(self, s=None):
        raise RuntimeError("nope")

my_list = user_list([11, 22, 33, 44, 55])
my_list.append(66)
"""

class user_string(UserString):

    def append(self, new):
        self.data = self.data + new

    def remove(self, s):
        self.data = self.data.replace(s, "")

text='apple orange grapes bananas pencil strawberry watermelon eraser'
fruits = user_string(text)

for word in ['pencil','eraser']:
    fruits.remove(word)

print(fruits)

