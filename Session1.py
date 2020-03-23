print("Ali")
x = 4
x = "a"
print(x)
print(10>9)
print(10<9)
a = [1,2,3]
print(a[-1])
b = (4,5,6)
print(b[-2])
c= {7,8,9,'d'}
print('d' in c)
d = {"name" : "Ali" ,
     "Age" : 32
     }
print(d)
"""i = 5
while i < 10 :
    print(i)
    if i == 6:
        break
    i+=1"""
j = 3
while j <10:
    j +=1
    if j == 7:
        continue
    print(j)

def func1():
    print("hi")
func1()

def func2(name):
    print("name is " + name)
func2("ali")
func2("yes")

def func3(child1, child2, child3):
    print("childs are :" , child1,child2,child3)
func3('a', 'b' , 'c')

x= lambda a : a + 10
print(x(5))

class MyClass():
    x = 'a'
p = MyClass()
print(p.x)

class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hi Mr " , self.name , self.age)

class MyClass2:
    var = 10
instance1 = MyClass2()
print(instance1.var)

class shape:
    size = 2
    def __init__(self,name,color):
        self.name= name
        self.color= color
shape1 = shape('rec', 'blue')
shape2 = shape('circle','red')
print(shape1.name,shape1.color)
shape1.radius = 20
del shape1.name
print(shape1.radius,shape1.color)
setattr(shape1,'radius',10)
print(shape1.radius,shape1.color)
print(hasattr(shape1,'name'))
print(getattr(shape1,'color'))