#single line comment
'''multi line comment
working'''
a=23
b=5
print("multiplication of a*b=",a*b)
print("division of a/b=",a/b)
print("addition of a+b=",a+b)
print("subtraction of a-b=",a-b)
print("remainder a%b=",a%b)
print("a/b",a//b)


#String
var1=5*"hello world\n"#five times
var2='my name is Sarvanan'
#concatenation
greetings=var1+var2
print(greetings)
#get a character from string
print(var2[-2])
#slicing
print(var2[-4:])
print(len(var2))


#lists
#single dimension lists
listname=["apple",1,0.2]
print(listname[0])
#multi dimension lists
listname2=[[2,3,4],[3,4,5]]
print(listname2[0][0])
print(len(listname))
#replace directly
listname[0]="mango"
print(listname)
del listname[0]
print (listname)
listname.append("rainbow")
print(listname)

#Tuples
tuplename=("apple","mango")
print(tuplename)
print(tuplename[0])


#Dictionary
dict_name={1:"one","2":"two","3":"three"}
print(dict_name[1])
dict_name[0]="zero"
print(dict_name[0])
print(dict_name.keys())
del dict_name[0]
print(dict_name)

#input
#if..elif
var1=input()
if var1=="1":
    print("one")
elif var1=="2":
    print("two")


#
fruits=["apple","mango","orange"]
for i in range(0,3):
    print(fruits[i])
x=0
while x<3:
    print(fruits[x])
    x = x + 1

#class and functions
class Employee:
    def print_name(self):
        print(self.empname)
    def __init__(self):
        self.empname="Sarvanan"
emp=Employee()
emp.print_name()