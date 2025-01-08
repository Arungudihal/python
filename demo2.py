def calculator(a,b):
 x=a+b
 y=a-b
 z=a*b
 v=a/b
 return x,y,z,v

res1,res2,res3,res4=calculator(a=10,b=2)
print(res1,res2,res3,res4)

def calculator(a,b):
	"""calculator()-this is actually performing addition,substraction,multiplication and divison"""
	x=a+b
	y=a-b
	z=a*b
	c=a/b
	return x,y,z,c
res1,res2,res3,res4=calculator(10,2)
print(res1,res2,res3,res4)
print(calculator.__doc__)

def power_off(num,power):
	return num**power
print(power_off(2,5))
print(power_off(5,2))

def power_off(num,power):
	return num**power
res1=power_off(num=2,power=5)

res2=power_off(power=5,num=2)
print(res1)
print(res2)

def power_off(num,power=2):
	return num**power
res1=power_off(2)
print(res1)
res2=power_off(3)
print(res2)
res3=power_off(5)
print(res3)
res4=power_off(5,3)
print(res4)

def submit_details(**details):
	print(details)

submit_details(name="rashmika",gender="female",marks="35",city="coorag")

def add(x,y):
	'''function performs Addition'''
	return x+y
def sub(x,y):
	'''function performs Substraction'''
	return x-y
def mul(x,y):
	'''functiotn performs Multiplication'''
	return x*y
def div(x,y):
	'''function performs Division'''
	return x/y


	




	
























