

# CREATE A MODULE

import accountmodul
accountmodul.new_salary(1000)                           # returns 1200.0


import accountmodul as am
am.new_salary(2000)                                     # returns 2400.0
am.salarys                                              # returns [1000, 2000, 5000, 7500, 6000, 3000, 4000, 8500]

from accountmodul import new_salary
new_salary(3000)                                        # returns 3600.0




# EXCEPTIONS

a = 10
b = 0
a/b         # ---->>>>> program stops                   # returns ZeroDivisionError: division by zero


try:
    print(a/b)
except ZeroDivisionError:    # the program continues to run
    print("Error")

