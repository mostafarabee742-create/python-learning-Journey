# while loop 
 # condition while 

# build a counter from 1 to 10 

count=1
while count<=10:
    print(count)
    count+=1
#
answer=''
while answer!='yes':
    answer=input('do you agree?(yes/no):')
    
print('thank you')


# while true 

while True:
    answer=input('do you agree?(yes/no):')
    if answer=='yes':
        break
print('thank you')

# update

attempts=0

while attempts<3:
        answer=input('do you agree?(yes/no):')
        if answer=='yes':
             print('we on the same page')
             break
        attempts+=1
else:
     print('3 strikes. you are out!')        

