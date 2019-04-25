class generator:

	def __init__(self):
		yield (self)



class Alphabet:

	def alpha_list(self):
		ord_of_a = 97
		list_of_alpha = []

		for i in range(26):
			list_of_alpha.append(chr(ord_of_a))       #i want to make each alphabet seperate and iterate the seperatly
			ord_of_a +=1

		#for loop that make new var ( "var_"+i) and assing one alphabet to each of them
		yield list_of_alpha

a = Alphabet()
b = a.alpha_list()
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))


