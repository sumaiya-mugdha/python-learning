collection1= {1, 2, 3, 4, 5, "mew"}
print(collection1)
print(type(collection1))

#set methods
collection1.add(5)
collection1.add(6)
collection1.remove("mew")
print(collection1)
collection1.add((10, 20, 30))
print(collection1)
print(len(collection1))
print(collection1.pop())
print(collection1)
print(collection1.clear())


#practice
given_sub= {"python","java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print("Needed classroom: "+str(len(given_sub)))

nset={9,"9.0"}
print(nset)
nset1={("int",9),("float",9.0)}
print(nset1)
