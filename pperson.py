class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

        print("Constructing the Person object")

    def __del__(self):
        print("The garbage collector is automatically destroying the object")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

# p1 = Person("Mark", 20, 6)
# print(p1.public_prop)
#
# # print(p1.name)    # Doesn't work
# # print(p1.__name)  # Doesn't work
#
# print(p1.name)
# print(p1.get_name())
# p1.set_name("Anna")
# p1.name = "Anna"
# print(p1.name)
# print(p1.get_name())
# print(Person.get_name(p1))
#
# p1.name = "Jake"
# print(p1.name)
# print(p1.get_name())
#
# print(p1.height)
# p1.height = 7
# print(p1.height)
#
# print("Script is ending")
