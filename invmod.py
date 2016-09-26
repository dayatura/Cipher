from math import floor

def inv_mod(n,b):
    t0 = 0
    t = 1
    n0 = n
    b0 = b
    q = floor(n0/b0)
    r = n0 - q * b0    
    while r > 0:
        temp = t0 - q * t
        if temp >= 0 :
            temp = temp % n
        else:
            temp = n - ((-temp) % n)
        t0 = t
        t = temp
        n0 = b0
        b0 = r
        q = floor(n0/b0)
        r = n0 - q * b0
    if b0 != 1:
        print (str(b) + " tidak memiliki modulo " + str(n))
    else:
        print ("(1/"+str(b)+") mod "+str(n)+" = " + str(t) + " mod " + str(n))

print ("format: (1/b) mod n = t mod n")
n = int(input("masukan nilai n: "))
b = int(input("masukan nilai b: "))
inv_mod(n,b)
