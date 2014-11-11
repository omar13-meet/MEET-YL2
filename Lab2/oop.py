class Animal():
	def __init__(self,name,age):
		self.name= name
		self.age= age
	def sleep (self):
		print self.name + " of " + str(self.age) + " is sleeping."
	def eat (self,food):
		self.food=food
		print self.name + " of " + str(self.age) + " is eating " + str(self.food)


class Bird(Animal):
	def __init__(self,name,age,wingscolor):
		Animal.__init__(self,name,age)
		self.wingscolor= wingscolor
	def fly(self):
		print self.name + " is flying mutha fucka."


class Dog(Animal):
	def __init__(self,name,age):
		Animal.__init__(self,name,age)
	def bark(self):
		print self.name + " is barking."


x=Bird("imawesome", "OVER 9000!!!!!", "red")
y=Dog("imdergenbern", 10000000)

x.sleep()
y.sleep()

x.eat("pizza")
y.eat("pizza")

x.fly()
y.bark()