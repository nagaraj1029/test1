#Recursive function :print n natural number
def print_num(n): 
    if (n == 0):
        return
    print(n)
    print_num(n-1)
   # print("in loop of num",n)
print_num(int(input("Eneter number:")))

#Recursive function :sum of n natural number
def calc_sum(n):
    if (n == 0):
        return 0
    return calc_sum(n-1) + n
sum = (int(input("Eneter number:")))
print("Sum of ",sum,"natural number :",calc_sum(sum))