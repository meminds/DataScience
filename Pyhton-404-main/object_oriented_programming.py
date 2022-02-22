

"""

Class : Classes are used to create groups with similar properties

class DataScience():
    
"""

#CLASS FEATURES

class DataScience():
    section = ''
    sql = 'YES'
    experience = 0
    languages = []


#access class properties
DataScience.section                     # returns ''
DataScience.sql                         # returns 'EVET'

#change class properties
DataScience.sql = "NO"
DataScience.sql                         # returns 'NO'




# INSTANTIATION

ali = DataScience()

ali.sql
ali.experience
ali.section
ali.languages.append("Pyhton") # changes main class
ali.languages                           # returns  ['Pyhton']
DataScience.languages                   # returns  ['Pyhton']



# help line 40 --->>> changes only instantiation
class DataScience():
    def __init__(self):
        self.languages = []



# DEFINE A METHOD

class DataScience():
    employees = []
    
    def __init__(self):
        self.languages = []
        self.section = ''
    
    def add_lang(self, new_lang):
        self.languages.append(new_lang)
        

# INHERITANCE

class Employees():
    def __init__(self):
        self.firstName = ''
        self.lastName = ''
        self.address = ''


class DataScience(Employees):
    def __init__(self):
        self.programming = ''


class Marketing(Employees):
    def __init__(self):
        self.storyTelling = ''

