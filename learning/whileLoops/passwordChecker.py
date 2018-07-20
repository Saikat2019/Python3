correctPassword="python3isnotworking"
password=input("enter your password\n")
name=input("please enter your name\n")
surname=input("please enter your surname\n")
while password!=correctPassword:
    print("please give the correct password\n")
    password=input("enter your password\n")
message="hi %s %s,you are logged in" %(name,surname)
print(message)
