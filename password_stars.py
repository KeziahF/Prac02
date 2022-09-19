min_length = 5
password = input("Password: ")

while len(password) < min_length:
     print("Invalid Password")
     password = input("Password: ")

for i in range(len(password)):
    print("*",end="")