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
    else:
      print("Contact your library for new registration")

def UserLogin():
    found=False
    user_list=[]
    user_list.append({"username": "silpa", "password": "aaa",})
    user_list.append({"username": "bruna", "password": "bbb",})
    user_list.append({"username": "megan", "password": "ccc",})
    user_list.append({"username": "sumaya", "password": "ddd",})
    user_name=input("Enter Username:  ")
    for user in user_list:
        if (user['username'].find(user_name)!=-1):
           pass_word=input("Enter password:  ")
           if (user['password'].find(pass_word)!=-1):
              found=True
              break
           else:
               found=False
               break
          
    if (found==True):
        print("Login Sucesssful")
        #DisplayMainmenu()
    else:
        print("Login Unsuccessful")
        #UserLogin()
    return

#calling function
        

LoginMenu()
