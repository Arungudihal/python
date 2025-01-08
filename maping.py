from functools import reduce

string=["apple","banana","cat","elephant"]
string=reduce(lambda x,y :x if len(x)>len(y) else y,string)
print(string) 