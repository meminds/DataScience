?print                                        # returns document


# How to write a function
def take_square(x):
    x**2                                      # returns Name Error             
take_square(5)                   

def take_square(x):
    print(x**2)                               # returns 25            
take_square(5) 



# function with information note
def take_square(x):
    print("Number entered: "+x**2)            # returns TypeError
take_square(3)

def take_square(x):
    print("Number entered: "+str(x**2))       # returns 'Number entered:' 9
take_square(3)



# function with two argument
def multiply(x,y):               
    print(x*y)                                # returns 42
multiply(6,7)



# predefined argument
def multiply(x, y=4):
    print(x*y)
multiply(3)                                   # returns 12
multiply(5,2)                                 # returns 10
multiply(y=3,x=7)                             # returns 21



# When to write a function
def direct_account(isi,nem,sarj):
    print((isi+nem)/sarj)                     # returns 1.25
direct_account(20,30,40)



#using function outputs as inputs 
def direct_account(isi,nem,sarj):
    print((isi+nem)/sarj)                     # returns 1.25
output = direct_account(20,30,40)
print(output)                                 # returns None
direct_account(20,30,40)*9                    # TypeError

def direct_account(isi,nem,sarj):
    return (isi+nem)/sarj
direct_account(20,30,40)                      # returns 1.25
direct_account(20,30,40)*9                    # returns 11.25



# local and global variables
x = 10      # global
y = 20

def multiply(x,y):
    # local
    return x*y



#change global domain from local domain
x = []
def add_x(y):
    x.append(y)
add_x(3)
add_x("ali")
add_x(25)
add_x(5)
add_x("veli")
x                                              # returns [3, 'ali', 25, 5, 'veli']

