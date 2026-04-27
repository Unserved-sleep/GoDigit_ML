from collections import ChainMap

dic1={'red':5,'black':1,'white':2}
dic2={'chennai':'tamil','delhi':'hindi'}
dic3={'firstname':'bob','lastname':'mathews'}

my_chain = ChainMap(dic1,dic2,dic3)
print(my_chain)
print(my_chain.maps)
print(my_chain["red"])
print(list(my_chain.keys()))
print(list(my_chain.values()))


new_dic={'blue':10,'yellow':12}
my_chain = my_chain.new_child(new_dic)
print(my_chain)
my_chain.maps = reversed(my_chain.maps)
print(str(my_chain))