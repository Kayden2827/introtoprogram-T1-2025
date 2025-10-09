#unit 3 chapter 2
a = 0
b = 11
c = 52

if a == 0:
    print("kiwi")

else:
    print("plum")



def checkpass():
    password = "firebird"
    password = input ("enter password\n>")
    if password == "firebird":
        print("welcome")



    else:
        print("wrong pass")
        checkpass()
        
checkpass()