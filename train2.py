import sys
print(sys.argv)
#print(sys.argv[1])
def say_hello(name):
    print("hello {}, the data scientist".format(name))

if __name__ == '__main__':
    say_hello(sys.argv[0])