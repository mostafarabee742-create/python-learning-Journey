# conditional statenents
 # if statement
  # basic form (single if statement)

score=50
if score>=90 :
    print('A')

# if_else statement 

score=50
if score>=90 :
    print('A')
else:
    print('F')    

# if_elif_else

score=80
if score>=90 :
    print('A')
elif score>=80:
    print('B') 
else:
    print('F')    

# if_elif_elif_else

score=68
if score>=90 :
    print('A')
elif score>=80:
    print('B') 
elif score>=70:
    print('C')
elif score>=60:
    print('D')        
else:
    print('F')     

# nesting (if_else)

score=95
submitted_project= True
if score>=90 : 
    if submitted_project: # if the first if true
        print('A+')
    else:    # if the first if true and second one is false 
        print('A')
elif score>=80:  # if the first if is false 
    print('B') 
elif score>=70:
    print('C')
elif score>=60:
    print('D')        
else:
    print('F')    

# logical operators 

score=50
submitted_project= True
if score>=90 and submitted_project: 
         print('A+')
elif score>=90:
    print('A')
elif score>=80:   
    print('B') 
elif score>=70:
    print('C')
elif score>=60 or submitted_project:
    print('D')        
else:
    print('F')    


# independed (if_else)

score=50
submitted_project= True    

if score>=90:
    print('High score')
else:
    print('low score')

if submitted_project:
    print('project is submitted')
else:
    print('no project')


# Task 1

email = "baraa@gmail.com"

# Clean the String
email = email.strip()

# Email must not be empty
if email == "":
    print("Email cannot be empty.")
# Email must contain a '.' and '@'
elif not ('.' in email and '@' in email):
    print("Email must contain . and @")
# Email must contain exactly one '@' symbol
elif email.count('@') != 1:
    print("Email must contain exactly one @.")
# Email must end with '.com', '.org', or '.net'
elif not email.endswith(('.com', '.org', '.net')):
    print("Email must end with .com, .org, or .net")
# Email must not be longer than 254 characters
elif len(email) > 254:
    print("Email must not be longer than 254 characters")
# Email must start and end with a letter or digit
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a letter or digit")
else:
    print("Email is valid.")


# task 2
#Validate the Quality and Correctness of Passwords

password='123SAa45678'
# Clean the String
#password=password.strip()
# Must not be empty
if password == '':
    print('password connot be empty')
#Must be at least 8 characters 
elif len(password)< 8:
    print('password must be at least 8 characters') 
 #Must not be same as the email  
elif password==email:
    print('its weak password change it') 
 #Must not contain any spaces 
elif not(password == password.strip()):
    print('password cannot have any spaces')
#Must start and end with a letter or digit  
elif not(password[0].isalnum() and password[-1].isalnum):
    print('password must start with letter or digit')
 #Must include at least 1 uppercase
elif not any(ch.isupper() for ch in password):
    print("Password must include at least one uppercase letter.")
 #Must include at least 1 lowercase  
elif not any(ch.islower() for ch in password):
    print("Password must include at least one lowercase letter.")    
else:
    print('password is valid')


 
 
 

