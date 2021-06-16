import os

def ClearScreen():
   os.system('cls')

def LoginMenu():
    ClearScreen()
    print("Menu Options")
    print(" 1:  User Login")
    print(" 2:  User Registration")
    choice=int(input("Enter your choice:  "))
    if(choice==1):
      UserLogin()
    return
def UserLogin():
    user_list=[]
    user_list.append({"username": "silpa", "password": "aaa",})
    user_list.append({"username": "bruna", "password": "bbb",})
    user_list.append({"username": "megan", "password": "ccc",})
    user_list.append({"username": "sumaya", "password": "ddd",})
    user_name=input("Enter Username:  ")
    for user in user_list:
        if (user['username'].find(user_name)!=-1):
           break
    pass_word=input("Enter password:  ")
    for pw in user_list:
        if (pw['password'].find(pass_word)!=-1):
           break

    print("Login Sucesssful")
        

LoginMenu()
