lst=[{"name":"arun","age":25},{"name":"kumar","age":24},{"name":"mantu","age":40}]
result = list(map(lambda person: person["name"].upper(), filter(lambda person: person["age"] > 25, lst)))

print(result)
