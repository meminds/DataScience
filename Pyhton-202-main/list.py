
"""
                      LIST DATA STRUCTURE 

[]
list()

replaceable
inclusive
sequential

"""


notes = [90,80,70,50]
type(notes)                                #returns list
list = ["a",19.3,90]
list_wide = ["a",19.3,90,notes]

len(list_wide)                             # returns 4
type(list_wide[0])                         # returns str

list_wide[0]                               # returns 'a'
list_wide[1]                               # returns 19.3
list_wide[3]                               # returns [90,80,70,50]

all_list = [list,list_wide]                
all_list                                   # returns [['a', 19.3, 90], ['a', 19.3, 90, [90, 80, 70, 50]]]

"""
del all_list                               # delete all_list
del list_wide
del list
del notes
"""



list = [10,20,30,40,50]

list[1]                                    # returns 20
list[6]                                    # returns IndexError
list[0:2]                                  # returns [10, 20]
list[:2]                                   # returns [10, 20]
list[2:]                                   # returns [30, 40, 50]


new_list = ["a",10,[20,30,40,50]]

new_list[0:2]                               # returns ['a', 10]
new_list[3]                                 # returns IndexError
new_list[2]                                 # returns [20, 30, 40, 50]
new_list[2][1]                              # returns 30
new_list[2][3]                              # returns 50


list = ["ali","veli","berkcan","ayse"]

list[1]                                     # returns 'veli'
list[1] = "velis_father"                  
list                                        # returns ['ali', 'velis_father', 'berkcan', 'ayse']

list[1] = "veli"
list[0:3] = "alis_father","velis_father","berkcans_father"
list                                        # returns ['alis_father', 'velis_father', 'berkcans_father', 'ayse']

list = ["ali","veli","berkcan","ayse"]

list + ["kemal"]                            # returns ['ali', 'veli', 'berkcan', 'ayse', 'kemal']
list                                        # returns ['ali', 'veli', 'berkcan', 'ayse']
list = list + ["kemal"]             
list                                        # returns ['ali', 'veli', 'berkcan', 'ayse', 'kemal']


#          append && remove

list = ["ali","veli","ayse"]

list.append("berk")
list                                        # returns ['ali', 'veli', 'ayse', 'berk']
list.remove("berk")
list                                        # returns ['ali', 'veli', 'ayse']



#           insert && pop

list = ["ali","veli","berkcan","ayse"]

list.insert(0,"ayse")
list                                        # returns ['ayse', 'ali', 'veli', 'berkcan', 'ayse']
list.insert(2,"mehmet")
list.insert(5,"berk")
list.insert(len(list),"yaren")
list                                        # returns ['ayse', 'ali', 'mehmet', 'veli', 'berkcan', 'berk', 'ayse', 'yaren']
list.pop(0)
list                                        # returns ['ali', 'mehmet', 'veli', 'berkcan', 'berk', 'ayse', 'yaren']





#       count
#       copy
#       extend
#       index
#       reverse
#       sort
#       clear



list = ['ayse', 'ali', 'ali', 'mehmet', 'veli', 'ali', 'berkcan', 'berk', 'ayse', 'yaren']

list.count("ali")                            # returns 3
list_backup = list.copy()
list.extend(["a","b",10])                    # add a,b,10
list.index("ali")                            # returns 1
list.reverse()                               # reverse printing
list.sort()                                  # returns TypeError

list = [10,40,5,90]
list.sort()
list                                         # returns [5, 10, 40, 90]
list.clear()
list                                         # returns  []










