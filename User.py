print("- WELCOME TO THE SYSTEM LOGIN ")
dic ('user1': "2021",
     'user2': "2022",
     'user3': "2023",
     'user4': "1234",
     'users': "4321",
     'user6': "1111",
     'user7': "0000",
     'users': "2222",
     'user9': "3333",
     'user10': "4444" )

username input("Enter username: ")

if username in dic :

    password = input("Enter password:-") 
    if dic[username] == password :

        print ("You are now logged into the system.")

    else:

        print ("Invalid password.")
else:
    print ("You are not valid user.")
