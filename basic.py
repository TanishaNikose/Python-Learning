# printing statement
print("Hey, I am learning Python.")

# writting multiple statement in one line.
print("Tanisha"); print("Nikose"); print("I am a girl.")

# If you want to print multiple words on the same line, you can use the end parameter:
print("Tanisha" , end=" ")
print("Nikose")

# You can also use the print() function to display numbers:
print(45)
print(3456)
print(23456)
print(70475437594375)
print(4*4) # can also perform airthmate operation
print("I am Tanisha Nikose and I am",2 , "years old.")

# multine comments :-   triple quotes me likhte h, agr variable me assign kr diya to as a variable treate hoge else multiline comment ki trh treate hoge.
"""
Hi  
I am tanisha.
"""

'''
Hi,
I am tani. 
'''

# variables :-  Variable names are case-sensitive.
x = 1
y = "john"
y1 = 'John'

# casting
x1 = int(3)
print(x1)
print(type(x1))  # tell us the time of the varible. 

x2 = str(4)
print(x2)
print(type(x2))

'''
Rules to Create Variables in Python

Variable name letter (a–z, A–Z) ya underscore (_) se start hona chahiye
✔ name = "Tanisha"
✔ _age = 22
❌ 1name = "Tanisha"

Numbers start me allowed nahi, but baad me use kar sakte hain
✔ user1 = "Aman"
❌ 1user = "Aman"

Sirf letters, numbers aur underscore (_) allowed hain
❌ Special symbols allowed nahi
❌ user-name
❌ marks@2026

Spaces allowed nahi hote
❌ first name = "Tanisha"
✔ first_name = "Tanisha"

Python case-sensitive hai
age aur Age different variables hain.

Python keywords variable name nahi ban sakte
❌ if = 10
❌ class = "DevOps"
(keywords: if, else, for, while, def, return, True, False, etc.)

Python me variable type declare karna zaroori nahi (Dynamic Typing)
x = 10
x = "hello" (same variable, new type)
'''


# Camel Case
myVaribleName = "Jin"
# Pascal Case 
Myvariablename = "pascal"
# snake case
my_variable_name = "snake"

# one value to multiple varibale
x , y , z = "I", "Love", "You"
print(x)
print(y)
print(z)

name1 = name2 = name3 = "General"
print(name1)
print(name2)
print(name3)

# unpack a collection
fruits = ["apple ", "banana ", "Papita "]
x1, x2, x3 = fruits
print(x1)
print(x2)
print(x3)
print(x1,x2,x3)
print(x1+x2+x3)



# # output variables
# x = 12
# y = "Tanu"
# print(y+x)  # give error data type are not suitable for adding 

x = 12
y = "Tanu"
print(y , x)


# global variable :-  variables which are created outside the function
# Type 1  
x = "awesome"
def my_fun():
    print(x)

my_fun()

# Type 2
x = "Tani"
def fun():
    x = "Tanisha"
    print(x)

fun()


x = "Tani" # global variable
def fun(): 
    x = "Tanisha"  # Local variable
    return x
    
name = x 
print(name)


# To create a global variable inside a function, you can use the global keyword.
def myfun():
    global x
    x = "Tanu"
    
myfun()
print(x)


x = 10
def fun(): # agr ye fun run nhi hoga to x ki value 10 hi rhegi
    global x
    x = 12    

fun()
print(x)

# Python Data Type
