length = 33
iter_ = (x for x in range(length))  #0,1,2
c = 0
while 1:
    try :
        print(next(iter_))
    except StopIteration :
        break

howkteam = {'name' : 'Kteam', 'kter':69}
# list_values = list(howkteam.items())

# print(list_values)
# print(list_values[0])
# print(list_values[1])
for key, value in howkteam.items():
    print(key,'=>', value)
    # if (key ="Kteam")
    # break

s = 'How Kteam'
for ch in s:
    if ch == ' ':
        break
    else :
        print(ch)

for k in (1,2,3) :
 print(k)
 if k%2 == 0 :
     break
else :
    print('Done!')


lst = [5,(1,2,2), {'abc', 'xyz'}]
for i in range(len(lst)) :
    print(i)


lst = []
for a, b, c in [('how', 'kteam','Education'), ('chia', 'se', 'FREE')]:
    a = a.capitalize()
    b = b.upper()
    c = c.lower()
    lst.append('--'.join((a, b + c)))
print(lst)


student_list = ['Long', 'Giau', 'Trung', 'Thanh']

for idx, student in enumerate(student_list, 9):
    print(idx, '=>', student)

#xu ly ham
kter ='kter'
def kteam(age, text = kter) :
    print(age)
    print(text)
kteam(10,'Hello Kteam')

#Function
def f(kteam= []) :
    kteam.append('F')
    print(kteam)
f()
f()
f()
f()

#
# def kteam(a,b,c,d):
#     pass #
# kteam(3,'Free Eduction', d=1, c=5)
# print(stored([3,4,1], reverse = True))


def Teo(a, b=2, c=3, d =4):
    f = (a + d) * (b+c)
    print(f)
Teo(2,4,5,6)


def kteam1(k,t,e,*,r='Kter'):
    print(k)
    print(t,e)
    print('end', r)

lst = ['123', 'Kteam', 69.96]
# kteam1(lst[0], lst[1], lst[2], lst[3])
kteam1(*lst, r= 'K9')

#tupes
def kteam2(*args, kter):
    # print(args)
    # print(type(args))
    print(kter)

# kteam2('Kteam', 69.96, 'Henry')

kteam2(*(x for x in range(70)), kter= 'a hi hi')


#dic : xuat key
def kteam2(a, b):
    print(a)
    print(b)
dic = {'name' : 'kteam', 'member':69}
kteam(*dic)



#dic : xuat value
def kteam2(name, member):
    print('name =>', name)
    print('member =>', member)
dic = {'name' : 'kteam', 'member':69}
kteam2(**dic)

#cach 2 xuat kieu for 
# def kteam3(*kwargs):
#    for key, value in kwargs.items():
#        print(key, "=>" , value)

# kteam3(name='Kteam', member= 69)

def make_global() :
    global x
    x = 1
def local():
    x = 5
    print('x in local', x)

    make_global()
    print(x)
    local()
    print()






        