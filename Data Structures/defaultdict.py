from collections import defaultdict
def_dict = defaultdict(object)
print(def_dict)
def_dict['fruit'] = 'orange'
def_dict['drink'] = 'pepsi'
print(def_dict)
print(def_dict['drink'])
print(def_dict['chocolate'])

def print_default():
    return 'value absent'
def_dict = defaultdict(print_default)
print(def_dict['chocolate'])



mydict = {'a': 'Apple', 'b': 'Ball'}
print(mydict.get('c', 'NOT PRESENT'))
print(mydict.get('a', 'NOT PRESENT'))

