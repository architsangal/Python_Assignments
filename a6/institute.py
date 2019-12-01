from student1 import *

class Institute:

    students=[]

    def __init__(self,list_of_obj=[]):
        self.students = list_of_obj

    def isStudentOf(self,s):
        if s in self.students:
            return True
        else:
            return False
    
    def isAddable(self,s):
        if self.isStudentOf(s):
            return False
        else:
            return True

    def addStudent(self,s):
        if self.isAddable(s):
            self.students.append(s)
            return True
        else:
            return False