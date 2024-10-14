"""lst = [22,22,55,77,3,7,3,7]
cities = ["cj","kfhkdf","ufiud]"]

def print_len():
    print(len(cities))
    print(lst,end = " \t ")
    print(cities)

print_len()"""


def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(fact)
#calc_fact(int(input("Eneter the number for Fcatorial calc: ")))

def calc_usd_inr(usd):
    for i in range(1,usd+1):
        inr = usd * 83
    print(usd,"$(USD) =",inr,"₹(Indian Rupee)")
calc_usd_inr(int(input("Enter the number of USD: ")))
num = 3
def odd_even(num):
    if (num %2 == 0):
        print("EVEN number")
    else:
        print("ODD number")
odd_even(int(input("Enter the number : ")))