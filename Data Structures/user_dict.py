from collections import UserDict

'''
my_dict={'red':'5','white':2,'black':1}
user_dict = UserDict(my_dict)
print(user_dict.data)


class user_dict(UserDict):
    def pop(self, default=None):
        raise RuntimeError('no pops')

data = user_dict({'red':'5','white':2,'black':1})
data.pop('red')
'''


class user_dict(UserDict):
    def replace(self, key):
        self[key] = '0'

file = user_dict({'red': '5', 'white': 2, 'black': 1, 'blue': 4567890})

for i in ['blue', 'yellow']:
    file.replace(i)

print(file)

