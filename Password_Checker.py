print("Welcome to Password Checker App")

create_password = int(input("Create your new Password here: "))
print("Great Password!")

enter_password = int(input("Enter the Passoword you created: "))

if enter_password == create_password:
    print("Great your Entered Password is correct!")

if enter_password != create_password:
    print("Error Your Entered Password is Wrong, Try Again")
    again_enter_password = int(input("Enter the Passoword you created here again: "))
    if again_enter_password == create_password:
        print("Great The Passwod Entered is Correct")
    if again_enter_password != create_password:
        print("The Entered Password is not Correct, Try Again")
        final_enter_password = int(input("Again Enter the Password: "))
        if final_enter_password == create_password:
            print("Great The Password Matched")
        if final_enter_password != create_password:
            print("Sorry The password is wrong and now you cannot enter the password again!")    