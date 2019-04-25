class generator:

	def __init__(self):
		yield (self)



class Alphabet:

	def alpha_list(self):
		ord_of_a = 97
		list_of_alpha = []
		list_of_num   = []

		for i in range(26):
			list_of_alpha.append(chr(ord_of_a))
			ord_of_a +=1

		for a in range(len(list_of_alpha)):
			list_of_num.append(a)

			#assing variable and list item DYNAMICLLY

		#making a dict with key:num and value:alphabet
		self.dict = dict(zip((list_of_num),(list_of_alpha)))

		for k,v in self.dict.items():
			exec("%s=%s" % (k,v))



#make obj then check dynamic variable
#find a way to use next meathod for each variable

