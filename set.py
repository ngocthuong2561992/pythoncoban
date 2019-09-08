set_2 = {(1,2), (3,4)}
print(set_2)

set_3 = {value for value in range(3)}
print(set_3)
print(type(set_3))

set_2 = set('How Kteam')
print(set_2)
print(type(set_2))


set1 = {1,2,4,5,6}
set2 = {3,4}

set3 = set1 & set2
set4 = set1 | set2
set5 = set4 - set3

print(set3)
print(set4)
print(set5)