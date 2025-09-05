class RegisterStudent:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 


    def fulldetails(self):
        return f"{{firstname: {self.firstname} lastname: {self.lastname} age: {self.age}}}"
    



student1 = RegisterStudent("israel", "moses", 13)

student2 = RegisterStudent("John", "Doe", 22)

print(student1.fulldetails())
print(" ")
print(student2.fulldetails())
