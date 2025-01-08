numbers=[15,30,10,45,60,22]
result=list(filter(lambda x:x%3==0 and x%5==0,numbers))
print(result)