a = [[1,2,5],[5,6,7],[8,9,10]]

print(a)

#list rong
a = [i for i in range(30)]
print(a)

a = [[n,n*1,n*2] for n in range(1,4)]
print(a)

a = list([1,2,3])
print(a)

b = [1,2]
b = b + ['one', 'two']

print(b)


c = [1,2,'a','b','c',[3,4]]
cc = c[1:3]
print(cc)

ct = [1,1,1,4,8,9,10]
ctA = ct.count(1)
ctB = ct.index(4)
print(ctA)
print(ctB)

#chen them phan tu
ct.append([4,5])
print(ct)
ct.extend([4,5,[7,8]])
print(ct)


ct.insert(-2,9)
print(ct)


aaa = [1,4,6,78]
print(aaa)

ccc = aaa.pop(1)
print(aaa)
print(ccc)


cccc = [8,89,79,7]
print(cccc)

cccc.sort()
print(cccc)
