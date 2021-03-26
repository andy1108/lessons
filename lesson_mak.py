#print("Hello World")
#print(7) #argument is something you pass into a function for it to be used

#dogname = "Bob"
#print(dogname)

#three types of variables

# #String variable - e.g. text
# name = "Andrea"

# #Int variable - e.g. whole number
# age = 18
# age = 18.5 

# #Boolean variable - e.g. True/False
# isMale = True

# print(dogname)
# print(dogname)
# print(dogname)
# print(dogname)

# myName = "Mak"
# age = 18 
#print("My age is" + " " + str(age)) #joining strings together

# addition, subtraction, division, multiplication, powers

#print(int(15/3))
#==, !=, <, >, <=, >=

# age = 22
# if age > 21:
# 	print("You can drink - legally!")
# elif age == 21:
# 	print("You can just drink")
# else:
# 	print("You're not old enough to drink")

# while condition:
# 	do something until the condition is no longer true

# age = 1
# while age <= 21:
# 	print(age)
# 	age += 1

# grade12 = ["Andrea", "John", "Bob", "Mike"]
# #iterate
# for name in grade12:
# 	if name == "Andrea":
# 		print("Hey that's me!")
# 	else:
# 		print(name)


# def McDonalds(client_order, earnings):
# 	print(client_order, earnings)

# order = "Big Mac"
# amount_paid = 4
# McDonalds(order, amount_paid)

# def introducing_myself(username, userage):
# 	print_my_name(username)
# 	print_my_age(userage)

# def print_my_name(name):
# 	print("Hi there I'm " + name)

# def print_my_age(age):
# 	print("I'm " + age)

# introducing_myself("Andrea", "19")
# introducing_myself("Mak", "18")

# def even_nums(start, end):
# 	if start % 2 == 0:
# 		print("Even - " + str(start))
# 	if start != end:
# 		even_nums(start+1, end)

# even_nums(1,11)

class Human():
	def __init__(self, name, gender, cityofbirth, dadname, momname):
		self.name = name
		self.gender = gender
		self.cityofbirth = cityofbirth
		self.dadname = dadname
		self.momname = momname
	
	def introduce_myself(self):
		print("Hi! I'm " + self.name)
	
	def change_my_name(self):
		new_name = input("Enter " + self.name + "'s new name: ")
		self.name = new_name


Andrea = Human("Andrea", "M", "Turin", "Paul", "Carmen")
John = Human("John", "M", "Boston", "George", "Laura")

Andrea.introduce_myself()
Andrea.change_my_name()
Andrea.introduce_myself()
