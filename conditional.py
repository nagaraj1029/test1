age = 20
#"int(input("enter the number:"))"
if(age>=18):
    print("apply for DL")
elif(age<18):
    print("Wait till eligibily for DL")

marks = float (input("Eneger the marks: "))
if(marks >90):
    grade = "A"
elif(marks >=80 and marks <=90):
    grade = "B"
elif(marks >70 and marks < 80):
    grade = "C"
else:
    grade = "D"
print("Grade of the Student:",grade)
