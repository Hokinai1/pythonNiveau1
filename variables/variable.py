
# x = 6

# def afficher ():
#     global x
#     a = x *2
#     print(x)
    
# afficher()

# print(x)
a = 1
def f() :
    print(a)
def g() :
    a=2
    print(a)
def h() :
    global a
    a=3
    print(a)
print(a)
f()
print(a)
g()
print(a)
h()
print(a)
    