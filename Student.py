class Student():
    name = 'abc'
    grade='5th'
    age='7'

    def display(self):
        print("name from Student is ",self.name)
        print("Grage from Student is ", self.grade)
        print("age from Student is ", self.age)

class School(Student):

    def SchoolStudentDisplay(self):
        print("name from School is ",self.name)
        print("Grage from School is ", self.grade)
        print("age from School is ", self.age)

#Calling Student object
obj = Student()
obj.display()

#Calling School object
obj = School()
obj.SchoolStudentDisplay()