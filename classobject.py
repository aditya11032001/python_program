class student:
    def __init__(self,name,rollno):
        self.n=name
        self.m=rollno
    def myprint(self):
        print("Name :",self.n)
        print("Roll No :",self.m)
obj1=student("aditya mishra","09")
# obj1.myinput("Aditya Mishra")
obj1.myprint()
