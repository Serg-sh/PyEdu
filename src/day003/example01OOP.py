class Person:
    name = None
    age = None

    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def set(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' : ' + str(self.age)


vlad = Person()
vlad.set('Vlad', 25)

print(vlad)


class Student(Person):
    course = None

    def __init__(self, name=None, age=None, course=None):
        super().__init__(name, age)
        self.course = course


    def set(self, name, age, course):
        super().set(name, age)
        self.course = course

    def setCourse(self, course):
        self.course = course

    def __str__(self):
        return super().__str__() + ' : ' + str(self.course)


ivan = Student()
ivan.set('Ivan', 18, 1)

print(ivan)
print(Student('Kolya', 21, 4))


def decorator(func):
    def qwerty():
        print('1')
        func()
        print('2')
    return qwerty


@decorator
def show():
    print('0000')


show()
