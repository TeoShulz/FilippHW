class Person:

	COUNTER = 1000

	def __init__(self, name: str, age: int) -> None:
		self.__name = name
		self.__age = age

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, age: int) -> None:
		self.__age = age

	@classmethod
	def change_counter(cls):
		Person.COUNTER += 1000
		COUNTER = Person.COUNTER
		return COUNTER




tom = Person('Tom', 25)
print(tom)
print(tom.age)
tom.age = 36
print(tom.age)
print(tom.change_counter())
print(tom.COUNTER)

molly = Person('Molly', 12)
print(molly.COUNTER)
