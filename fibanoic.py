def fibonacci(n):
	a,b=(0,1)
	print("fibonacci series:")
	for i in range(n):
		print(a,end="")
		a,b=b,a+b
n=int(input("enter the number of terms of fibonacci series:"))
fibonacci(n)