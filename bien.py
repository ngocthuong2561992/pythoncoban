a = 1.13454546466666776744

print (a)

print (type(a))

#chen comment decimal
from decimal import*

getcontext().prec = 30

f= 10/3
print(f)

d= Decimal(10)/Decimal(3)
print(d)

from fractions import*

frac1 = Fraction(6,9)
frac2 = Fraction(5,10)
frac3 = frac1 + frac2
print(frac1)
print(frac2)
print(frac3)
print(type(frac3))

c  = complex(2,5)
print(2+5j)

strHowKteam = """HowKteam.com\nFree education\nShare to be better"""
print(strHowKteam)

#nhan so chuoi
strB = strHowKteam*5
print(strB)


strA = "HowkTeam"
strB = "K"
#strB = strA[1:len(strA)]
#strB = strA[None : 5]
#lay ca chuoi
#strB = strA[None : None]
#strB = strA[:]
#strB = strA[None : 5:2]
#strB = strA[None : None:2]
strB = strA[None : 5:-1]
strC = strB in strA
#kt true or false
print(strB)
print(strC)


strAA = "69"
strBB = 69
strCC = int(strAA) + strBB
print(strCC)

strAAA = int(6.9)
print(strAAA)

strAAAA = "HowKteam.com"
strAAAA = strAAAA[None:1] + "0" + strAAAA[2:None]
print(strAAAA)
print(hash(strAAAA))


k = 'Kteam'
result = f'{k} - Free education'
print(result)

r = '1 : {1}, 2 : {0}'.format(111,222)
print(r)

team = 'hteam'
# b = team.center(5)
bteam = team.capitalize()
print(bteam)


team1 = '     co gi hot'
bteam1 = team1.join(['1','2','3'])
bteam2 = team1.strip()
bteam3 = team1.strip('c')
bteam4 = team1.replace('o','kteam',2)

teamString = 'cbco gi hotcbc'
teamStringB = teamString.lstrip('cb')

print(bteam1)
print(bteam2)
print(bteam3)
print(bteam4)
print(teamStringB)



#split
splitA = 'how kteam free education'
splitB = splitA.split(' ',1)
splitC = splitA.split(' ',2)
print(splitA)
print(splitB)
print(splitC)

#parition
partitionA = 'How kteam free education'
partitionB = partitionA.partition('k')
print(partitionA)
print(partitionB)













