a = float (input("Eneter the 1st number:"))
b = float (input("Eneter the 2nd number:"))
c = float (input("Eneter the 3rd number:"))

def cal_sum(a,b,c):
    return a+b+c
def cal_avg(a,b,c):
    return cal_sum(a,b,c)/3

sum = cal_sum(a,b,c)
print(sum)
avg = cal_avg(a,b,c)
print(avg)


