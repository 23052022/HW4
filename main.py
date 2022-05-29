x =int(input("Enter a number:"))
a = 0
for i in range(2, x//2+1):
    if (x % i == 0):
        a = a + 1
    if (a<= 0 ):
       print("is simple")
    else:
       print("is not simple")