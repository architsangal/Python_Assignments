class Student:
    name=""
    rollNumber="imt2020"
    xxx=""
    i=1
    def __init__(self,n):
        self.name = n
        if(Student.i<9):
            xxx="00"+str(Student.i)
        elif(Student.i<99):
            xxx="0"+str(Student.i)
        else:
            xxx=Student.i
        self.rollNumber=self.rollNumber+str(xxx)
        Student.i+=1
