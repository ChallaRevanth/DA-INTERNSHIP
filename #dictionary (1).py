#dictionary
std_details={'name':'revanth','rollno':553,'ph_no':7208372737,'gender':'male','isActive':True,'skills':['html','JS','css'],'address':{'city':'hyd','pincode':500037},'name':'sv'}

print(std_details)
print(std_details['name'])
std_details['ph_no']=548358554
print(std_details)
std_details['skills'].append('python')
print(std_details.get('name'))
print(std_details.keys())
print(std_details.values())
std_details['name']='ram'
std_details['gender']='male'
print(std_details)
std_details['skills'].pop()

num=int(input('enter a number:'))
if num%2!=0:
    print('odd number')

AGE=int(input('enter your age:'))
if AGE>=18 and AGE<=25:
    print('you are eligible to vote')




emp_details={'name':'revanth',
             'role':'developer',
             'experience':4,
             'salary':40000000
             }
if emp_details['role']=='developer' or emp_details['role']>'BDA':
    print(emp_details)


emp_details={'name':'revanth',
             'role':'developer',
             'experience':4,
             'salary':40000000
             }
role=int(input('enter your role:'))
emp_details={'name':'revanth',
             'role':'developer',
             'experience':4,
             'salary':40000000
             }
if emp_details['role']=='developer' or emp_details['role']>'BDA':
    print(emp_details)
    print(emp_details)
