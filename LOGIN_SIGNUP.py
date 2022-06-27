import json
import re


print("***WELCOME TO SIGNUP AND LOGIN***")

file=open("Login_system.json","r")
a=list(json.load(file))

choose=input("choose sign up or login")
if choose=="signup":
    username=input("enter your name:-")
    phoneNo=int(input("enter your phone number:-"))
    age=int(input("ejnter your age:-"))
    description=input("enter your description:-")
    hobby=input("enter the hubby:-")
    password=input("enter your password:-")
    
    for i in password:

        if len(password)>=6 and len(password)<=12:

            if not re.search('[A-Z]',password):

                print('please include a upper acse letter')

                break
            if not re .search('[a-z]' , password):

                print('please include a lower case letter')

                break
            if not re.search('[0-9]',password):

                print('please include include a digit')

                break
            if not re.search('[!@#\$%\^&\*]',password):

                print('please include a special charector')

                break
            else:
                print('strong password')
                break
        else:
            print('wrong length')

            
    confirmpassword=input("confirm your password")
    dic1={'username':username,'phoneNo':phoneNo,'age':age,'description':description,'hobby':hobby,'password':password}
    a.append(dic1)
    if password==confirmpassword:
        print("Registration sussfully")
        my_file=open("Login_system.json","w")
        json.dump(a,my_file,indent=6)
    else:
        print("registration failed! please cofirm your password correct ")
elif choose=='login':
    username=input('enter your name:')
    password=input('enter your password:')
    my_file=open("Login_system.json",'r')
    a=json.load(my_file)
    b={}

    def login_or_not(username,password,a,b):
        for i in a:
            if i['username']==username and i['password']==password:
                b.update(i)
                for k,v in b.items():
                    print(k,'is-',v)
                print('login sucessfully')
                break
            elif i not in a:
                print('login failed! plese enter your correct info...')
    Data=login_or_not(username,password,a,b)
else:
    print('incorrect')



    