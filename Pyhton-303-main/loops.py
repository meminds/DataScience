
# FOR loop
student = ["ali","veli","isik","berk"]

for i in student:    
    print(i)                               """returns ali
                                                      veli
                                                      isik
                                                      berk """
                                         
# Example --- Code that gives 20% increase in salaries.

salary = [1000,2000,3000,4000,5000]
for i in salary:
    print(i)

def new_salary(x):
    print(x*20/100 +x)

for i in salary:
    new_salary(i)                          """ returns 1200.0
                                                       2400.0
                                                       3600.0
                                                       4800.0
                                                       6000.0   """
                                                 
                                                 

# Break & Continue

salary = [8000,5000,2000,1000,3000,7000,1000]
salary.sort()
salary                                     # returns [1000, 1000, 2000, 3000, 5000, 7000, 8000]
    

for i in salary:
    if i==3000:
        print("stop")
        break
    print(i)                               """ returns 1000
                                                       1000
                                                       2000
                                                       stop  """

for i in salary:
    if i==3000:
        continue
    print(i)                               """ returns 1000
                                                       1000
                                                       2000
                                                       5000
                                                       7000
                                                       8000  """





# while

number = 1
while number<10:
    number += 1
    print(number)                          """ returns 2
                                                         3
                                                         4
                                                         5
                                                         6
                                                         7
                                                         8
                                                         9
                                                         10  """          

