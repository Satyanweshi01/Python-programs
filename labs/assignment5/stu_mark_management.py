#10. Student Marks Management: Write a Python program to store the names and marks of five students in a dictionary and display:
#The name and marks of each student.
#The student who scored the highest marks.
#The average marks of all students.

d = {}
for i in range(3):
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    d[name] = marks

for i in d.keys():
    print("Student Name: ",i,end=" ")
    print("Marks: ",d[i])

h_s_name = list(d.keys())[list(d.values()).index(max(d.values()))]
s = sum(list(d.values()))
a = s/len(d)

print("The student with highest marks: ",h_s_name)
print("The average marks :" ,a)