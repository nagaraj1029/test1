f = open("demo.txt","r")
fdata = f.readlines()
print(fdata)
print(type(fdata))
f.close()
for i in fdata:
    print(i)