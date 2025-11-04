# data types 

text='hi'
number=20

# type() function
print(type(text))
print(type(number))

#len() function
print(len(text))
# print(len(number))  # not work with intgers 

#upper() method for string  class
print(text.upper())

# bit_length() method for intger class
print(number.bit_length()) 

# string functions 
 # types 

name='mostafa' 
age=22
print(type(name))
print(type(age))

print('my age is'+ str(age))
age= str(age)
print(type(age))

# math

password='sasa11dgs'

print(len(password))

if len(password)<10 :
    print('your password is too short ')

text=''' 
python is easy to learn
Pyhton is powerfull
many people ioves Python'''

print(text.count('python'))


# transformations
#replace()
price='1234,56'

print(price.replace(',','.'))

print(price.replace(',','')) # we can use it to remove char in the text


number="+49(176)123-4567"

print(number.replace('+','00').replace('(','').replace(')','').replace('-',''))

# concatnation

folder='c:/users/sasa/'
file='report.csv'

full_file_path=folder+file

print(full_file_path)

# F string method 

name='mostafa'
age=22

print(f'my name is {name} and iam {age} years old .')

# split()

csv_file="1234,sasa,egypt,24-10-2003,M"

print(csv_file.split(',')) # output will be list of strings

# indexing & slicing

text="python"

print(text[0])
print(text[5])

print(text[0:3]) 
print(text[3:])
print(text[:3])

#cleaning
 #remove spaces
  # lstrip() & rstrip() & strip()

name="  mostafa"   
print(name.lstrip())

name="mostafa  " 
print(name.rstrip())

name="  mostafa  " 
print(name.strip())

name="@@mostafa@@" 
print(name.strip('@'))

#lower()  & upper()

text="python PROGRAMMING"

print(text.lower())
print(text.upper())

# clean before search 

search="Email "
data='emAIl'

print(search==data)

search="Email ".lower().strip()
data='emAIl'.lower().strip()

print(search==data)

# task 

text='968-Maria,  (d@t@ Engineer);; 27y  ' 

text=text.replace('968-','name:').replace('(','role:').replace('@','a').replace(');;','age:').replace('y','')

print(text)


text = "968-Maria, ( D@t@ Engineer );; 27y"

# 1. إزالة الأرقام والعلامات الغريبة من البداية
text = text.lstrip("0123456789-")

# 2. تقسيم النص على الفواصل لفصل الاسم عن الوظيفة والعمر
parts = text.split(",")
name = parts[0].strip().lower()

# 3. استخراج الوظيفة والعمر من الجزء الثاني
role_age = parts[1]

# 4. إزالة الأقواس والعلامات الغريبة
role_age = role_age.replace("(", "").replace(")", "").replace(";", "").strip()

# 5. تقسيم بين الوظيفة والعمر
role_part, age_part = role_age.split(" 27y")[0], "27"

# 6. تنظيف النص داخل الوظيفة
role = role_part.replace("D@t@", "data").strip().lower()

# 7. الطباعة بالشكل المطلوب
print(f"name: {name} | role: {role} | age: {age_part}")
