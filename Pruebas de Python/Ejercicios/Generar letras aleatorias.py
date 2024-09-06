import random,string

def Arr(x,y):
	return chr(random. randint(ord(x), ord(y)))
Aux=[]
print ("Arreglo de forma matricial")
for i in range(5):
	print("")
	for i in range(5):
		r=Arr("a","z")
		print(r,end=("-"))
		if r == "a" or r == "e" or r == "i" or r == "o" or r == "u":
			Aux.append(r)
print("\n")
print ("La cantidad de vocales es de: ",len(Aux))