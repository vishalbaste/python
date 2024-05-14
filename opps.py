class Student:
    def __init__(self,name,marks):
        self.marks = marks
        self.name = name
    
    def getMarksAvg(self):
        sum = 0
        for val in self.marks:
            sum += val
        
        print("Marks Average is :",sum / 5)

    @staticmethod
    def sayHello():
        print("Hello World");


s = Student("Vishal",[10,20,30,40,50])
s.sayHello()
s.getMarksAvg()