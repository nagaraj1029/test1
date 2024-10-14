n = int(input("Enter number"))
#m = int(input("Enter multiples of num"))
i = 1
"""while i <= n:
    print(i*n)
    i=i+1"""
"""for i in range(1,m+1): #Multiplication
    print(i*n)"""
for x in range(2,n+1):  # Least divisable number
    if n%x == 0:
        print(x)
        break