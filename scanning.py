class Book:
	def __init__(self, s):
		self.id = s

	def index():
		print("book")

class Library:
	def __init__(self,ids):
		self.id=ids
		print("Library id:{}",format(self.id))

	def init_head_data(self,data0,data1,data2):
		self.number_of_differents_books=data0
		self.signup_process=data1
		self.number_books_by_day=data2

	def init_books(self,data):
		books_library=[]
		print("Books Library id:{}",format(self.id))
		for book in data:
			books_library.append(book)
			print(book)
		self.books_library=books_library

	def get_books(self):
		return self.books_library	

class Time:
	def __init__(self, days):
		self.days = days

class Signup:

	def __init__(self,number_of_differents_books,number_of_libraries,number_of_day):
		self.number_of_differents_books=number_of_differents_books
		self.number_of_libraries=number_of_libraries
		self.number_of_day=number_of_day

	def set_libraries(self,libraries):
		self.libraries=libraries
		self.signup_active='N'
		print("Libraries")

	def process(self):

		for l in self.number_of_libraries:
			library=l

		if self.signup_active=='T':
			return 0
		else:
			# tutaj się odbywa to skanowanie, czekanie na kolej zczytania książki itp.
			for l in self.libraries:
				for b in l.get_books():
					print(b)

my_libraries = []
for library in range(2):
	my_libraries.append(Library(library))

file1 = open('a_example.txt', 'r') 
Lines = file1.readlines() 
file1.close()

number_of_differents_books=Lines[0].strip()[0]
number_of_libraries=Lines[0].strip()[2]
number_of_day=Lines[0].strip()[-1]
    
print(number_of_differents_books)
print(number_of_libraries)
print(number_of_day)
print("================");
order_books=[]
for book in Lines[1]:
	if book==' ' or book=='\n':
		continue
	order_books.append(book)

print("Scores of books:")
print(order_books)	

my_libraries[0].init_head_data(Lines[2].strip()[0],Lines[2].strip()[1],Lines[2].strip()[2])
my_libraries[0].init_books(Lines[3])

my_libraries[1].init_head_data(Lines[4].strip()[0],Lines[4].strip()[1],Lines[4].strip()[2])
my_libraries[1].init_books(Lines[5])

signup = Signup(number_of_differents_books,number_of_libraries,number_of_day)
signup.set_libraries(my_libraries)
print("================");
signup.process()
