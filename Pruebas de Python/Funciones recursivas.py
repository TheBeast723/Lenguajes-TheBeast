def Cuenta(num):
    if num>0:
        print (num)
        Cuenta (num-1)
    else:
        print ("BOOM")

Cuenta(78)