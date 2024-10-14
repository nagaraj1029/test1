with open("demo1.txt","r") as f:
    data = f.read()

new_data = data.replace("python","Advanced python")
print(new_data)

with open("demo1.txt","w") as f:
    f.write(new_data)