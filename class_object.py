Student.py  # create a class

class Student :

    def __init__(self, name, major, gpa. is_on_probation):
        self.name = name
        self.major = major
        self.gpa - gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):   # remember about SELF
        if self.gpa >= 3.5:
            return True
        else:
            return False


#==================================next class like app.py

# from Student import Student    // from Studen file import Student class

Student1 = Studemy("Jim", "Business", 3.1, False)   # student object
Student2 = Studemy("Pam", "Art", 3.1, True)   # student object



print(student1.name)
print(student1.on_honor_roll())

