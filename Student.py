from Person import Person

class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)
        self.major = major
        print("This time it's a Student object")

    def __del__(self):
        print("Deleting the Student object")

s1 = Student("Maria", 22, 6, "Computer Science")
print(s1.name)

