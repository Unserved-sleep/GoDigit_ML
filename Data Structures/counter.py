import collections

numbers = [1, 2, 3, 4, 5, 1, 5, 4, 1, 2]
num_counter = collections.Counter(numbers)
print(num_counter)

string = "lalalalandismagic"
string_count = collections.Counter(string)
print(string_count)


line = 'he told her that her presentation was not that good'
list_of_words = line.split()
line_count=collections.Counter(list_of_words)
print(line_count)


print(collections.Counter(numbers).most_common(2))
print(collections.Counter(numbers)[2])
print(collections.Counter(numbers)[-1])