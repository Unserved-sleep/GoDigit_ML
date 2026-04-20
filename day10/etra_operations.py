school_Friends = ['John', 'Alice', 'Bob', 'David']
college_Friends = ['Alice', 'Charlie', 'David', 'Eve']

print(set(school_Friends) | set(college_Friends))
print(set(school_Friends).union(set(college_Friends)))
print(set(school_Friends) - set(college_Friends))
print(set(school_Friends).difference(set(college_Friends)))
print(set(school_Friends) & set(college_Friends))
print(set(school_Friends).intersection(set(college_Friends)))
print(set(school_Friends) ^ set(college_Friends))
print(set(school_Friends).symmetric_difference(set(college_Friends)))
print(set(school_Friends) <= set(college_Friends))
print(set(school_Friends).issubset(set(college_Friends)))
print(set(school_Friends) >= set(college_Friends))
print(set(school_Friends).issuperset(set(college_Friends)))
print(set(school_Friends) == set(college_Friends))
print(set(school_Friends).isdisjoint(set(college_Friends)))
print(set(school_Friends) < set(college_Friends))
