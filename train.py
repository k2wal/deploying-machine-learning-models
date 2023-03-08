
import sys
print(sys.argv)
#print(sys.argv[1])
def say_hello(name):
    print("hello {}, the data scientist".format(name))

say_hello("ketan")

print('Numbers')


def two(x,y):
    #x = int()
    #y = input()
    d = int(x) + int(y)
    print(d)

x= sys.argv[1] 
y = sys.argv[2] 

two(x,y)


