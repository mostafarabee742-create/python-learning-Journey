# loops
 # for loop
 
for i in (1,2,3,4,5): # tuple sequance 
    print(f'round:{i}')

items=[1,2,3,4,5]  # list sequance
for item in items:
    print(f'round:{item}')   

items='mostafa'  # string sequance
for item in items:
    print(f'round:{item}') 

items= range(5)  # Range function sequance (1)
for item in items:
    print(f'round:{item}') 

items= range(1,5)  # Range function sequance (2)
for item in items: 
    print(f'round:{item}')    

items= range(1,10,2)  # Range function sequance (3)
for item in items: 
    print(f'round:{item}')  


# use case (transfor data)

files=['  reporT.csv','DATA.csv','FInal.txt']
for file in files:
    file=file.strip().lower().replace('txt','csv')
    print(f'processing {file}')

# task 1
for x in range(1,11):
    result=7*x
    print(f'7*{x}={result}')

#task 2

for i in range(1,7):
    print('*'*i)

# Advanced for loops 
 # break statement 

names=['sasa','mostafa','','rabee']
for name in names:
    if name =='':
        print('empty name')
        break
    print(f'name ={name}')

# contineue statement 

names=['sasa','mostafa','','rabee']
for name in names:
    if name =='':
        print('empty name')
        continue
    print(f'name ={name}')

# pass statement

names=['sasa','mostafa','','rabee']
for name in names:
    if name =='':
        pass #todo: handle empty value
    print(f'name ={name}') 

# use case(1) : skip weekends in calendar loop 

days=['mon','sun','wed','tue']
weekends=['sat','sun']
for day in days :
    if day in weekends :
        continue
    print(f'workday:{day}')

# use case(2):scan emails to block unsafe data from entering your system 

emails=[
    'data@gmail.com',
    'sasarabee@outlook.com',
    'drop table users;',
    'maria@gmail.com'
]

for email in emails :
    if ';' in email:
        print('hacker attack')
        break # dont trust this source any more 
    print(f'processing email:{email}')

# else inside for loops 

items=[1,2,4,5,7]
for item in items :
    print(item)
else: # uselese withot break statement 
    print('the loop is completed')    
 
# else with break statement 

# check for even number  
items=[1,2,4,5,7]
for item in items :
    if item % 2 ==0:
      print('even no. found:',item)
      break
else: 
    print('All number are odd')  

# check for missing names in a list use case(1):

names=['sasa','mostafa',None,'rabee']

for name in names:
    if name is None:
        print('empty name founded')
        break
else:
    print('all names are avaiable')    

# use case(2): check if all files are csv files

files=[ 'data1.csv',
       'report.txt',
       'data2.csv']
for file in files :
    if not file .endswith('.csv'):
        print('not all files are csv')
        break
else:
    print('all files are csv')

# task : check if any filename appears more than once 

files=['report.csv', 'data.xlsx',
       'summary.docx',
       'report.csv',
       'data.csv'] 

for file in files :
    if files.count(file)>1:
        print('Duplicate found')
        break
else:
    print('all files are uniqe')    

# nested for loops 

for x in range(3):# outer loop
     for y in range(2): #inner loop 1
         for z in range(2): # inner loop 2
             print(f'({x},{y},{z})')
    
# use case 1 : crossing data 

colors=['red','blue','green']
sizes=['L','M','S']

for color in colors:
    for size in sizes:
        print(f'{color} - size {size}')

# use case 2: hierarchy

years=[2026,2027]
months=['jan','feb']
days=range(1,29)
 
for y in years: # level 1
    for m in months: # level 2
        for d in days : # level 3
            print(f'report_{y}_{m}_{d}.csv')

# use case 3 : navigate thriugh tables & columns 

 # select count(*)from customers where id is null;

tables=['customers','orders','products','prices']
columns=['id','create_id']

for t in tables:
    for c in columns: # بدل ماتكتب كل الكويري يدوي في sql 
        print(f'select count(*)from {t} where {c} is null;')
