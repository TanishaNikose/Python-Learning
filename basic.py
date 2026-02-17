# # printing statement
# print("Hey, I am learning Python.")

# # writting multiple statement in one line.
# print("Tanisha"); print("Nikose"); print("I am a girl.")

# # If you want to print multiple words on the same line, you can use the end parameter:
# print("Tanisha" , end=" ")
# print("Nikose")

# # You can also use the print() function to display numbers:
# print(45)
# print(3456)
# print(23456)
# print(70475437594375)
# print(4*4) # can also perform airthmate operation
# print("I am Tanisha Nikose and I am",2 , "years old.")

# # multine comments :-   triple quotes me likhte h, agr variable me assign kr diya to as a variable treate hoge else multiline comment ki trh treate hoge.
# """
# Hi  
# I am tanisha.
# """

# '''
# Hi,
# I am tani. 
# '''

# # variables :-  Variable names are case-sensitive.
# x = 1
# y = "john"
# y1 = 'John'

# # casting
# x1 = int(3)
# print(x1)
# print(type(x1))  # tell us the time of the varible. 

# x2 = str(4)
# print(x2)
# print(type(x2))

# '''
# Rules to Create Variables in Python

# Variable name letter (a–z, A–Z) ya underscore (_) se start hona chahiye
# ✔ name = "Tanisha"
# ✔ _age = 22
# ❌ 1name = "Tanisha"

# Numbers start me allowed nahi, but baad me use kar sakte hain
# ✔ user1 = "Aman"
# ❌ 1user = "Aman"

# Sirf letters, numbers aur underscore (_) allowed hain
# ❌ Special symbols allowed nahi
# ❌ user-name
# ❌ marks@2026

# Spaces allowed nahi hote
# ❌ first name = "Tanisha"
# ✔ first_name = "Tanisha"

# Python case-sensitive hai
# age aur Age different variables hain.

# Python keywords variable name nahi ban sakte
# ❌ if = 10
# ❌ class = "DevOps"
# (keywords: if, else, for, while, def, return, True, False, etc.)

# Python me variable type declare karna zaroori nahi (Dynamic Typing)
# x = 10
# x = "hello" (same variable, new type)
# '''


# # Camel Case
# myVaribleName = "Jin"
# # Pascal Case 
# Myvariablename = "pascal"
# # snake case
# my_variable_name = "snake"

# # one value to multiple varibale
# x , y , z = "I", "Love", "You"
# print(x)
# print(y)
# print(z)

# name1 = name2 = name3 = "General"
# print(name1)
# print(name2)
# print(name3)

# # unpack a collection
# fruits = ["apple ", "banana ", "Papita "]
# x1, x2, x3 = fruits
# print(x1)
# print(x2)
# print(x3)
# print(x1,x2,x3)
# print(x1+x2+x3)



# # # output variables
# # x = 12
# # y = "Tanu"
# # print(y+x)  # give error data type are not suitable for adding 

# x = 12
# y = "Tanu"
# print(y , x)


# # global variable :-  variables which are created outside the function
# # Type 1  
# x = "awesome"
# def my_fun():
#     print(x)

# my_fun()

# # Type 2
# x = "Tani"
# def fun():
#     x = "Tanisha"
#     print(x)

# fun()


# x = "Tani" # global variable
# def fun(): 
#     x = "Tanisha"  # Local variable
#     return x
    
# name = x 
# print(name)


# # To create a global variable inside a function, you can use the global keyword.
# def myfun():
#     global x
#     x = "Tanu"
    
# myfun()
# print(x)


# x = 10
# def fun(): # agr ye fun run nhi hoga to x ki value 10 hi rhegi
#     global x
#     x = 12    

# fun()
# print(x)

# # Python Data Type
# x = "Hello World"
# print(type(x))

# y = 12
# print(type(y))

# z = 3.4
# print(type(z))

# p = 1j
# print(type(p))

# q = ["Tani", "Tanu", "Tanisha"]
# print(type(q))

# r = (1,2,3,4)
# print(type(r))

# s = range(5)
# print(s)
# print(type(s))

# d = {"name" : "Tanisha", "Surname" : "Nikose"}
# print(d)
# print(type(d))

# a = {"apple", "banana", "Papita"}
# print(a)
# print(type(a))

# a1 =  ({"apple", "banana", "Papita"})
# print(type(a1))
# print(print(a1))

# b = True
# print(type(b))

# b1 = b"Hello"
# print(type(b1))

# b2 = bytearray(5)
# print(b2)
# print(type(b2))

# byte ko change nhi kr skte, bytearray ko change kr skte h 

# m = memoryview(bytes(5))
# print(m)
# print(type(m))

# x = None
# print(x)
# print(print(x))

# # Setting the Specific Data Type
# xS1 = str("Hello World")
# print(type(xS1))

# xS2 = int(20)
# print(type(xS2))

# xS3 = float(20.5)
# print(type(xS3))

# xS4 = complex(1j)
# print(type(xS4))

# xS5 = list(("apple", "banana", "cherry"))
# print(type(xS5))

# xS6 = tuple(("apple", "banana", "cherry"))
# print(type(xS6))

# xS7 = range(5)
# print(type(xS7))

# xS8 = dict(name="john", age=36)
# print(type(xS8))

# xS9 = set(("apple", "banana"))
# print(type(xS9))

# xS10 = frozenset(("apple", "banana"))
# print(type(xS10))

# xS11 = bool(10)
# print(type(xS11))

# xS12 = bytes(12)
# print(type(xS12))

# xS13 = bytearray(5)
# print(type(xS13))

# xS14 = memoryview(bytes(5))
# print(type(xS14))

# #  Quick Question :- check pallindrome 

# checkpalindrome  = 1221
# num = checkpalindrome
# result  = 0
# while num > 0:
#     remainder = num % 10
#     result = (result*10) + remainder
#     num = num // 10

# if  checkpalindrome == result:
#     print("palindrome")
# else:
#     print("Not Pallindrome")

# # quick Question :-  Check if a number is armstrong number 
# print("ARMSTRONG NUMBER")

# n = 1634
# num = n
# nod = len(str(n))
# arm = 0
# while num > 0:
#     remainder = num % 10
#     arm = (remainder ** nod ) + arm
#     num = num // 10

# if n == arm:
#     print(" armstrong Number ")
# else:
#     print("Not Armstrong Number")

# Python Numbers

x = 1
y = 1234567890123456789012345678901234567890
z =-1234567898765432
print(type(x))
print(type(y))
print(type(z))

x1 = 1.12345
y1 = 1.0
z1 = -34.2345
x2 = 35e3
y2 = 12E4
z2 = -87.7e100
print(type(x1))
print(type(y1))
print(type(z1))

e1 = 3+5j
e2 = 5j
e3 = -5j
print(type(e1))

p1 = 1
p2 = 2.8
p3 = 1j

p11 = float(p1)
p22 = int(p2)
p33 = complex(p1)

print(p11, p22, p33)
print(type(p11))
print(type(p22))
print(type(p33))

# note - complex number ko kisi bhi type me change kiya ja skta h 
# agr hme koi rander number chahiye to hmare pass koi randon method nhi h, we have module for this and we can use it 

import random
print(random.randrange(90))
print(random.randrange(0,10))


# # Quick questions :-  factors of a number 
# num = 20
# result = []
# for i in range(1, num+1):
#     if num % i == 0:
#         result.append(i)
        

# print(result)
# # tc - o(n) sc - o(k) k refers to the number of factors. The Time complexity is very High lets find the better way

# num = 20 
# result = []
# for i in range(1, num//2):
#     if num % i == 0:
#         result.append(i)

# result.append(num)
# print(result)

# # tc - o(n/2) lets find more better way 
 
# from math import sqrt
# num = 36
# result = []
# for i in range(1, (int(sqrt(num)+1))):
#     if num % i == 0:
#         result.append(i)
#         if num//i != i:
#             result.append(num//i)

# result.sort()
# print(result) 


# # Quick Question - find the freqency of the number 
# num = [5,6,7,7,1,9,111,1,1,5,1,1]
# freq_map = {}
# for i in range(0, len(num)):
#     if num[i] in freq_map:
#         freq_map[num[i]] += 1
#     else:
#         freq_map[num[i]] = 1

# print(freq_map)

# # second method for find the frequency of the number -
# num = [5,6,7,7,1,9,111,1,1,5,1,1]
# hashmap = {}
# for i in range(0, len(num)):
#     hashmap[num[i]] =  hashmap.get(num[i],0) + 1
# print(hashmap)

# Python casting
x = float(1) 
a = x
x = str(1)
b = x
print(a,b)

# python strings
print("His name is 'Tanay'")
print('His name is "Tanay"')
print("It's all right")

# agr hm is multiline string ko kisi variable me store nhi krege to yeh ek multiline comment ki tarah treate hoga
para ='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(para[0])
print("Lorem" in para) # true
print("And" not in para) # true
print(para[:4])
print(para[3:10])
print(para[-15:-1])
print(para.upper())
print(para.lower())
print(para.strip()) # remove white space form begining and end

a = "He,llo"
print(a.replace("H", "T"))
print(a.split(",")) # jaha separeator milega waha pr se array bna dega ex:-  ['He', 'llo']

# # loop through a string 
# for i in para:
#     print(i)


