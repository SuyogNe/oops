class student:
    name="Suyog"
    grade=8

    def intro(self):
        print("hello, I am from Nepal")

    def inner(self):
        print("My name is ",self.name)
        print("I am from grade ",self.grade)

s=student()
s.intro()
s.inner()