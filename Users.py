userList = []


userList.append({"IDNumber": "01", "isLibrarian": False, "Username": "IvanCooper", "Password": "1237", "Name":"Ivan", "Surname": "Cooper", "BorrewedBooks":[]})
userList.append({"IDNumber": "02", "isLibrarian": False, "Username": "FionaMurphy", "Password": "2450", "Name":"Fiona", "Surname": "Murphy", "BorrewedBooks":[1,2]})
userList.append({"IDNumber": "03", "isLibrarian": False, "Username": "AoifeWalsh", "Password": "2753", "Name":"Aoife", "Surname": "Walsh", "BorrewedBooks":[4]})
userList.append({"IDNumber": "04", "isLibrarian": False, "Username": "BrendanO'Brien", "Password": "2745", "Name":"Brendan", "Surname": "O'Brien", "BorrewedBooks":[]})
userList.append({"IDNumber": "05", "isLibrarian": False, "Username": "PeterO'Neill", "Password": "2457", "Name":"Peter", "Surname": "O'Neill", "BorrewedBooks":[]})
userList.append({"IDNumber": "06", "isLibrarian": False, "Username": "DeclanKennedy", "Password": "2821", "Name":"Declan", "Surname": "Kennedy", "BorrewedBooks":[6,8,9]})
userList.append({"IDNumber": "07", "isLibrarian": True, "Username": "RyleeLynch", "Password": "0415", "Name":"Rylee", "Surname": "Lynch", "BorrewedBooks":[3]})

def DisplayUsers():
    print("Library Users:")
    print("===========================================================")
    print(f"Id".ljust(8), "Username".ljust(20), "Name".ljust(20), "Surname".ljust(20))
    print("===========================================================")
    
    for user in userList:
        print(f"{user['IDNumber'].ljust(8)} {user['Username'].ljust(20)} {user['Name'].ljust(20)} {user['Surname'].ljust(20)}")

DisplayUsers()
