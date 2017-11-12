class animal(object):
	"""docstring for animal"""
	def __init__(self, name,sound, age, favorit_color):
		super(animal, self).__init__()
		self.sound = sound
		self.name = name
		self.age = age
		self.favorit_color = favorit_color

	def eat(self, food):
		print("yummyyy !! "+ self.name + " is eating" + food	)

	def make_s(self,a):
		print(self.sound*a)



class person(object):
	def __init__(self, name, age, gender, home_add, status, religion):
		self.name = name
		self.age = age
		self.gender = gender
		self.home_add  = home_add
		self.status = status
		self.religion = religion
	def breakfast()
		

frog = animal("frog"," Quack!", 6, "green")
frog.eat(" fly")
frog.make_s(10)

moshe = person("Moshe Rabeno", 120, "male", "Eygipt land", "slave", "Jowish")

print(frog)

		