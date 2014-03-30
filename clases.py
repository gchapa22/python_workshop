
class Animal(object):
	def __init__(self):
		self.attr = 1

	def speak(self):
		return "Noise"

class Dog(Animal):
	def speak(self):
		return "Waw"

	def bite(self):
		return "chomp"

class Cat(Animal):
	def speak(self):
		return "Miau"

fido = Dog()
pelusa = Cat()

print fido.speak()
print pelusa.speak()
