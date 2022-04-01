

a=10
def indentation():
#local variable	a=15
	print("in", a)
indentation()
#global variable 
print("out", a)


a=10

print(id(a))

def indentation():

	global a
	print(id(a))

	a=15

	print("in", a)

	print(id(a))

indentation()

print("out", a)

