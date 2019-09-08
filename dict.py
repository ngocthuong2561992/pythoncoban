dic = {'name' : 'Kteam', 'member':69}
print(dic)
print(type(dic))

# dicA = dic('Kteam'='HowKteam', 'FE'='Free education')
# print(dicA)
# print(type(dicA))


dicB = dict(K=69, HK='HowKteam', FE='Free Education')
print(dicB)

dicB['K'] = dicB['K'] + 1
print(dicB)

dicC = {'Team':'Kteam',(1,2): 69}
print(dicC)

value = list(dicC.items())
print(value[1])

#default
# valueCC = dicC.setdefault('WhatUpGuys', 'Hey')
valueCC = dicC.update(Team = 'Free Education')

print(valueCC)
print(dicC)



