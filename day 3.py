# string functions 
  # search 
   # startwith() & endwith() & in operator

phone='+48-167-12345'
print(phone.startswith('+47'))

email='mostafarabee742@gmail.com'
print(email.endswith('gmail.com'))

print('@'in email)

# find()

phone1='+123-456-6666'
phone2='+345-123-3333'
phone3='+399-499-8787'

print(phone1[5:]) # static sol
print(phone1.find('-')) # find the index of (-)
print(phone1[phone1.find('-')+1:]) # dynamic sol 
print(phone2[phone2.find('-')+1:])
print(phone3[phone3.find('-')+1:])

# numeric functions 
  # types
# type()
x=22
y=3.7
z=2+3j

print(type(x))
print(type(y))
print(type(z))
   
#int()

x='24'
print(type(x))
print(x*3)

x=int(x)
print(type(x))
print(x*3)

# operators

print(2+3)
print(2*5)
print(6-3)
print(7/2)  # normal divided 
print(7//2) # floor division (rounds the reuslt)
print(10%3) # % remainder used to check if the num is even 
print(2**3) # ** it means 2 to the power 3

x=2 
x+=3 # x=x+3
print(x)
 
# rounding numbers 

import math # math is module 
price=38.94568594

print(round(price)) 
print(round(price,2))

print(math.floor(price))
print(math.ceil(price))

print(math.trunc(price)) 
print(int(price))


# Random module functions  
 
import random

print(random.random())
print(random.randint(2,4))

# validatation

p=4.00
print(p.is_integer())

t=7.2
print(t.is_integer())

x=70
print(isinstance(x,int))

# task 
import random
x= random.randint(1,100) # generate a ramdom interge between 1 and 100
print(x)

if x % 2 == 0 : # check if it an even or not 
 print('x is even')
else:
 print('x is odd') 


 