
#               NUMBERS AND STRINGS


print(9)                       # int value
print(9.2)                     # float value
print(9+9)                     # addition
print(9*9)                     # multiplication
print(9/9)                     # division
print(9-4)                     # extraction process
print("HELLO AI ERA")          # string expression





# tpye()  function
numberone = 9
numbertwo = 9.2
stringg = "HELLO AI ERA"
type(numbertwo)                # returns int
type(stringg)                  # returns str

type(123)                      # returns int
type("123")                    # returns str

"a"+"b"                        # returns 'ab'
"a""b"                         # returns 'ab'
"a" "b"                        # returns 'ab'
                               # "a" - "b"    ------>>>  ERRORRRR
                               
                               
                               

#access length information
a = "i am writing in python"
len(a)                         # returns 22



#Case conversions  upper & lower
a.upper()                      # returns 'I AM WRITING IN PYTHON'
a.isupper()                    # returns False
a.islower()                    # retuns True

a.lower()                      # returns 'i am writing in python'
a.isupper()                    # returns True
a.islower()                    # retuns False


#character change
a.replace("i", "e")            # returns e am wreteng en python




#Character Trimming Operations
b = "*hello*"
b.strip("*")                   # returns 'hello'



dir(b)
"""
 RETURNS 
 
 ['__add__',
 '__class__',
 '__contains__',
 '__mul__',
 '__ne__',
 '__str__',
 '__subclasshook__',
 'capitalize',
 'isdecimal',
 'isdigit',
 'isidentifier',
 'islower',
 'isnumeric',
 'rpartition',
 'rsplit',
 'rstrip',
 'split',
 'splitlines',
 'startswith',
 'strip',
 'swapcase',
 'title',
 'translate',
 'upper',
 'zfill']  
"""
                               




#substrings
a[0]                            # returns 'i'
a[5]                            # returns 'w'
a[0:5]                          # returns 'i am '
a[6:11]                         # returns 'ritin'


"""
#type conversions
one_number = input()
type(one_number)                # returns str
int(one_number)                 # returns int value
float(12)                       # returns 12.0
str(14)                         # returns '14""
"""




# use print()
print("future","write")                  # returns future write
print("future","write",sep="_")          # returns future_write
#?print
"""
Docstring:
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
"""


print("hello")




