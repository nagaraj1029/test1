def printlist(list,i=0):
    if (i == len(list)):
        return
    print(list[i])
    printlist(list,i+1)
#    print("priting list element",i)

veg = ["carrot","chlli","kfllf","brinjal","spinach","potato","beans",]
printlist(veg)