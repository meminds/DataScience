

"""
TUPLE 

no replaceable
inclusive
sequential

"""

t = ("ali", "veli",1,2,3.2,[1,2,3,4])
type(t)                                        # returns tuple

tt = "ali", "veli",1,2,3.2,[1,2,3,4]
type(tt)                                       # returns tuple

notup = ("eleman")
type(notup)                                    # returns str

tpl = ("eleman",)
type(tpl)                                      # returns tuple

t[1]                                    # returns 'veli'
t[0:3]                                    # returns ('ali', 'veli', 1)

t[3] = 99                                     # returns TypeError //// no replaceable



"""
DICTIONARY 

replaceable
inclusive
unordered

"""


dictionary = {"REG" : "Regresyon modeli",
              "LOJ" : "Lojistik Regresyon",
              "CART" : "Classification and Reg"}

type(dictionary)                                    # returns dict
len(dictionary)                                     # returns 3


dictt = {"REG" : ["RMSE",10],
         "LOJ" : ["MSE",20],
         "CART" :["SSE",30]}
type(dictt)                                         # returns dict


dictt[0]                                            # returns KeyError
dictt["REG"]                                        # returns ['RMSE', 10]


dictt = {"REG" : {"RMSE" : 10,
                  "MSE" : 20,
                  "SSE" : 30},
         "LOJ" : {"RMSE" : 10,
                  "MSE" : 20,
                  "SSE" : 30},
         "CART" : {"RMSE" : 10,
                  "MSE" : 20,
                  "SSE" : 30}}

dictt["REG"]                                        # returns {'RMSE': 10, 'MSE': 20, 'SSE': 30}
dictt["REG"]["SSE"]                                 # returns 30



dictionary = {"REG" : "Regresyon modeli",
              "LOJ" : "Lojistik Regresyon",
              "CART" : "Classification and Reg"}

# ADD
dictionary["GBM"] = "Gradient Boosting Mac"
dictionary[1] = "Artificial neural networks"
dictionary

# MODIFY 
dictionary["REG"] = "coklu dogrusal regresyon"
dictionary


l = [1] # list                          
dictionary[l] = "NEWWW"                             # returns TypeError (unhashable type: 'list')


t = ("tuple",) #tuple
dictionary[t] = "NEWWW"

dictionary                    
"""
{'REG': 'coklu dogrusal regresyon',
 'LOJ': 'Lojistik Regresyon',
 'CART': 'Classification and Reg',
 'GBM': 'Gradient Boosting Mac',
 1: 'Artificial neural networks',
 ('tuple',): 'NEWWW'}
"""









