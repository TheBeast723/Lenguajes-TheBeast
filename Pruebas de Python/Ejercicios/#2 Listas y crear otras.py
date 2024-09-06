Lista1 = [1,2,4,7,3,7,45,7,3,65,3,7,4,"Pollo"]
Lista2 = [56,3,7,3,7,3,6,3,5,3,7,36,5,"Pollo"]

print (Lista1)

Lista1 = set(Lista1)
Lista2 = set(Lista2)

Ambas = list (Lista1 | Lista2)

print (Ambas)

Ambas = list (Lista1 - Lista2)

print (Ambas)

Ambas = list (Lista2 - Lista1)

print (Ambas)

Ambas = list (Lista1 & Lista2)

print (Ambas)