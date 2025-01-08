lst=5,10
res=max(lst,key=lambda x:x)
print(res)

max=lambda(x,y,z : x if x>y and x>z else y if y>z else z)
print("The max value is : ",max(50,100,12))