class Person:
    def	__init__(self,name):
        self.name = name

    def	say_hi(self):
        print('Hello,my name is',self.name)
p = Person('Leo')
p.say_hi()

#	前面两行同时也能写作 #	Person('Swaroop').say_hi()
