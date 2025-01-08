from functools import reduce

lst=[1,2,3,4,5,6]
lst=reduce(lambda a,b : a+b,map(lambda i:i**2,filter(lambda x: x%2==0,lst)))


