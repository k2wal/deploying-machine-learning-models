
import sys
print(sys.argv)
#print(sys.argv[1])
def say_hello(name):
    print("hello {}, the data scientist".format(name))

#say_hello("ketan")

#print('Numbers')


def two(x,y):
    #x = int()
    #y = input()
    d = int(x) + int(y)
    print(d)

#x= sys.argv[1] 
#y = sys.argv[2] 

#two(x,y)

if __name__ == "__main__":
    args = sys.argv
    # args[0] = current file
    # args[1] = function name
    # args[2:] = function args : (*unpacked)
    globals()[args[1]](*args[2:])

