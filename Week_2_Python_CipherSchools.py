def show_loading():
    for _ in range(3):
        print("loading...")
a=5
b=7
print(a+b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()


def show_loading():
    for i in range(3):
        print("loading", "."*(1+i))
show_loading()

def sheldon_knock():
    for _ in range(3):
        print("knock knock knok penny")
sheldon_knock()

def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knok",name)
sheldon_knock("Harry")

def sheldon_knock(name, times=3):
    for _ in range(times):
        print("knock knock knok",name)
sheldon_knock("Harry")

def add(a, b):
    return a+b
a=add(1,3)
print(a)

print(1,3,4,5,6,7,sep="_")

def fun(a,b,c,d):
    print(a)
    print(b)
    print(c)
    print(d)
fun(c=0,b=1,d=4,a=5)

def hello():
    print("Hello World !")
    return 1
a=1
a=hello
a()

def fun(a,b):
    print(a,b)
fun(9,8)

def fun(a=1,b=9):
    print(a,b)
fun()
fun(1)
fun(6,7)

def fun(*a):
    print(a)
fun(1,2,3,4,5,6)

def fun(a,b,*c):
    print(a)
    print(b)
    print(c)
fun(1,2,3,4,5,6)

def fun(a,b,*c,d):
    print(a)
    print(b)
    print(c)
    print(d)
fun(1,3,44,5,6,7,78,6,"shivam",d=8)
    
def fun(a,b,*c,d,e="jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
fun(1,3,44,5,6,7,78,6,"shivam",d="Khushi",e="love")

def fun(**k):
    print(k)
fun(name="class")

a=1
b=2
c= print(a+b)
print(c)

def asdf():
    print("gibberish")
asdf()

print("Hello World")
show = print
show("something")

names=["jatin", "saransh", "shubham", "samarth"]
for a in enumerate(names):
    print(a)
    print(type(a))

a = 5
b = 9
a=a+b
b=a-b
a=a-b
print(a,b)

a = 5
b = 9
a,b = b,a
print(a,b)

a=[1,2]
b,c=a
print(b,c)

a=1,2
print(type(a))

names=["jatin", "saransh", "shubham", "samarth"]
scores = [50,90,60,80]
for i, name in enumerate(names):
    score = scores[i]
    print(name, "_", score)

names=["jatin", "saransh", "shubham", "samarth"]
scores = [50,90,60,80]
states = ["delhi", "punjab", "himachal", "odisha"]
for name, score, state in zip(names,scores,states):
    print(name, "-", score,state)

a=5
print("value of a is %d" % (a)) 
print("value of a is {}".format(a))

a,b,c,d=1,2,4,3
print("a={} ,b={},c={}".format(c,b,a))

a,b,c,d=1,2,4,3
print("a={2} ,b={1}, c={0}".format(c,b,a))

name="jatin katyal"
company="shuttl"
print("name= {name} company={company}".format(name=name,company=company))

print(f"name={name}")

name="jatin katyal"
company="shuttl"
print("Hello {name} welcome to my Facebook ".format(name=name,company=company))

print(f"name = {10/3}")

print(len(r"*a\nb"))
for c in r"a\nb":
    print(c)

print("   jatin    ".strip())
print("1, 2, 3, 4, 5, 6".split(","))
print("jatin katyal".replace("a","z"))
print("vidyasagar".count("a"))

a=[1,2,3,4,5]
print(a)

b=["jatin",1,1.5,print]
print(b)

a[0]=100
print(a)

print(len([1,4,5,6,7]))

print("jatin"+"katyal")
print([1,2,3]+[4,5,6])
print([1]*6)

a=[1,2,3,4,5,6]
for x in a:
    print(x)

print("z" in "jatin")
print(1 in [1,2,3,4])

a=[1,2,3,4,5,6]
print(a[-1])

a=[1,2,3,]
a.insert(1,100)
print(a)

a=[1,2,3,4]
a.append(9)
print(a)

a.pop()
print(a)

a.remove(3)
print(a)

a=[4,5,1,6,7,3,2,0]
a.sort()
print(a)
a.reverse()
print(a)

for x in reversed(a):
    print(x)

a=[1,2,3,4,8]
print(1,4,9,16,64)

for x in map(lambda x: x**2, a):
    print(x)

for i,x in enumerate(a):
    pass
def sqr(x):
    return x**2
print(a)

print(int('1'))

print(",".join(["jatin","samarth", "molly"]))

a=[1,2,3]
a[0]=100
a[2]=200
print(a)

a=(1,2,3,4)
print(type(a))

def fun(*args):
    print(type(args))
fun(1,2,3,4,5)

a=9
b=5
a,b=b,a
c=a,b
print(type(c))

def sum_diff(a,b):
    s=a+b
    d=a-b
    return s,d
s,d=sum_diff(10,5)
print(s,d)
print(type(c))
print(c)

a=(1,2,3,4)
print(list(a))
print(list(range(5)))
print(tuple(range(5)))
a=(9,8,7,6)
a=[9,8,7,6]
a.append(5)
a.append(3)
print(a)

a={
    "name": "Jatin Katyal",
    1:"something",
    (1,2): "tuple key wat?"
}
print(a["name"])
print(a[1])
print(a[1,2])

a={
    "name": "Jatin Katyal"
}
a["name"]= "gourav"
print(a)

a={
    "name": "Shivam Thakur",
    "company": "Google",
    "college": "LPU"
}
print(a["name"])
print(a["company"])
print(a["college"])

key = "marks"
if key in a:
    print(a[key])
else:
    print("key does not exist")

key= "marks"
print(a.get(key))

key ="marks"
print(a.get(key, "key does not exist"))
print(a.values())

for x in a.items():
    print(x)

for key, value in a.items():
    print(key, "->", value)

for x in a:
    print(a)

print(list(a))
print("name" in a)

a={1,2,3,4}
print(type(a))
print(list(a))

for i in a:
    print(i)

a.add(7)
a.remove(3)
a.add(2)

for i in a:
    print(i)

a={1,2,3,4,5}
b={3,4,5,6,7}
print(a-b)
print(a.union(b))
print(a.intersection(b))
a.add(1)
a.remove(4)
print(a)

a=[['']*6]*6
a[1][1]='x'
print(a)

print(id(a[0][1]))
print(id(a[1][1]))
print(id(a[2][1]))
print(id(a[2][2]))

a=[1,2,3,4,5]
print(id(1))
print(id(a))

a=258
b=258
print(a == b)
print(a is b)

a = []
for i in range(5):
    a.append(i)
print(a)

print([ i for i in range(5) ])
print( list(map(lambda x: x**2, range(5))))

a = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(j)
    a.append(temp)
print(a)

print([ i for i in range(5) for j in range(5) ])
print([ [j for j in range(5) ]  for i in range(5) ])

a=[]
for i in range(2):
    for j in range(2):
        a.append(j)
print(a)

print([ [] for i in range(5) ])
print([ [ (i,j) for j in range(2) ] for i in range(2) ])

print({
    2:4,
    3:9,
    4:16,
})

print({ i: i**2 for i in range(5)})

print({ i for i in range(5)})
print(type(a))

a= {i for i in range(5)}
print(type(a))

for x in a:
    print(x)

it = iter(a)
print(next(it))

student1 = {
    "name": "Jatin Kayyal",
    "marks": 50
}
student2 = {
    "name": "Samarth",
    "marks": 100
}
print(student1)

class Person:
    pass
p = Person()
print(p)
print(hex(id(p)))

class Person:
    def say_hi(self):
        self.name = " Nikhil"
        print('Hello, how are you' + self.name + "?")
p = Person()
p.say_hi()

a=1
print(a+1)
print(str(a))

class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person("Shivam")
p.say_hi()

class A:
    def __init__(self):
        print(self)
        print("initialized")
a=A()
print(a)

class A:
    def __init__(self):
        print(self)
        print("initialized")

    def __del__(self):
        print(self)
        print("I am dying")
a=A()
print(a)

a = 1
print(type(a))
print(a.__add__(7))
print("jatin" *6)
print("jatin".__mul__(2))

class A:
    a=1
    b=2
    def __add__(self, x):
        return self.a + self.b + x
a=A()
print(a)