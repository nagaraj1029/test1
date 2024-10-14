class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

        print("Addinf student")

    def hello(self):
        print("Hello")
    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum = sum + i
        print("sum:",sum,"Average:",sum/3)


s1 = student("Pie",[99,98,90])
print(s1.name)
s1.get_avg()
