# control flow 
 # Boolean expression 
  # values
print(True)
print(False)
print(type(True))

# functions # output true or false
 # bool()

print(bool()) 
print(bool(123))
print(bool(''))
print(bool('sasa'))
print(bool(None)) # None means no value
print(bool(0))
 
 # any() & all()
email=''
phone='01227453288'
username='mostafa74'

print(any([email,phone,username])) # true 
print(all([email,phone,username])) # false

email='sasa@gamil.com'
phone='01227453288'
username='mostafa74'

print(any([email,phone,username])) # true 
print(all([email,phone,username])) # true

# isinstance()
print(isinstance(123,int))
print(isinstance(True,str))

# comparison operators

print(10==10) # Equel
print(3!=3)   # not equal
print(7>2)    # grater than
print(5>=4)   # grater than or equal
print(2<9)    # less than
print(3<=3)   # less than or equal

# chained comparison
 # is age between 18 and 30 ?

age=17
print(18<=age<=30) # true

# Logical operators
# checks if the system is under pressure 

cpu_usage=70
memory_usage=95

print(cpu_usage>90 or memory_usage> 90) # Alert

# control mixed conditions

  # allow access only if the user is logged in 
  # or they are a guest
  # but they not be banned

is_logged_in= True
is_guest=False
is_banned=True

print(is_logged_in or is_guest and not is_banned) # True
# with parentheses()
print((is_logged_in or is_guest) and not is_banned) # false


# Task 
# 1- check if user_name is not empty and the age is greater than or equal to 18
user_name='mostafa74'
age=22

print(bool(user_name)and age>=18)

#2- check if the password is at least 8 characters long and dose not contain spaces

password='12323235' 

print(len(password)>=8 and # password at least 8
      password==password.strip() # password has no spaces
      ) 

#3- check if a user email is not empty , contains'@' and ends with '.com'

user_email="sasa33@gmail.com"

print(bool(user_email) and # email is not empty 
      '@'in user_email and #'@'in
      user_email.endswith('.com') # email end with '.com'
      )

#4-check if a username is a string , is not none and is longer than 5 characters 

user_name="mostafa99"

print(user_name==str(user_name) and # user name is string 
      bool(user_name)and # not empty or none 
      len(user_name)>5) # longer than 5
 

#5- check if the user is either an admain or moderator , and either thet are not banned or they have verified their email 

is_admain= True
is_moderator= False
is_banned= False
email_verified= True

print(is_admain or is_moderator) and ( not is_banned or email_verified) 

print(is_admain or is_moderator and  not is_banned or email_verified)

# membership operator 
 # in operator 

print('a'in 'mostafa')

print(6 in [2,3,9])

domain = 'spam.com'
banned_domains = ['spam.com','fake.org','bot.net']

print(domain not in banned_domains)

# identity operator
 # is operator 

x=[2,3,4]
y=[2,3,4]

print(x==y) # compare values
print(x is y) # compare id im the memory

x=[2,3,4]
y= x

print(x==y) 
print(x is y)

# make sure the email exists, and its not empty . 

email= None
print(email is not None and email != "" )  