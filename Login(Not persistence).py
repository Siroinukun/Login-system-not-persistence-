Verify = input("Type Y if you have Account, If wish to register, Type N: ")

while True:
    if Verify == ("N") or ("n"):
        Register = input("Enter your new Account name: ")
            
        if Register == (""):
            print("Please enter a name!")
            continue

        RegisterPassword = input("Enter your new Password!: ")
        if RegisterPassword == (""):
            print("Please enter a password!")
            continue
        elif RegisterPassword == (Register):
            print("Do not use same password as username!")
            continue
        else:
            print("Account Created successfuly!")
    break

while True:
    Account = input("Enter your account:" )
    if Account == (Register):
        print("Account Verified!")
        Loginned = (Account) or (Register)
        break
    else:
        print(Account, "not exist!")
        continue

while True:
    Password = input("Enter your Password:" )
    if Password == (RegisterPassword):
        print("Logined Successfuly!")
        break
    else:
        print("Password is wrong!")
        continue

print(Loginned, "Logined!")