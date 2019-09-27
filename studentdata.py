my_list=[]
class student:
    def __init__(self,sid,age,marks):
        self.sid=sid
        self.age=age
        self.marks=marks
    def validate_marks(self):
        if (self.marks>=0 and self.marks<=100):
            print("Marks of",self.sid," are valid")
            return True
        else:
            print("Marks of ",self.sid," are invalid")
            return False
    def validate_age(self):
        if (self.age>20):
            print("Age of",self.sid,"is valid")
            return True
        else:
            print("Age of ",self.sid," is invalid")
            return False
    def check_qualification(self):
        a=self.validate_marks()
        b=self.validate_age()
        if(a==True and b==True):
            if(self.marks>=65):
                print("Yay good student")
                return True
            else:
                return False
    def getdata(self):
        print("student id = ",self.sid)
        print("student age = ",self.age)
        print("student marks = ",self.marks)            

a=int(input("Enter student id"))
b=int(input("Enter student age"))
c=int(input("Enter student marks"))
s=student(a,b,c)
    


s2 = student(1,22,67)
s1=student(17,18,-79)

s.check_qualification()
s.getdata()
s1.check_qualification()
s1.getdata()
s2.check_qualification()
s2.getdata()

        
