
startcar = input ("what is the car you want\n>")#please say the saab 950
cash = 9000 #say 9999 to go to dev comand <make dev comands
print (cash)

def start ():#start here\/
    day1 = print ()
    print("you wake up to your car is broken")
    print("1. fix it")
    print("2. sell it and get a new one")
    print("3. go back to bed")
    choice = input("> ")

    if choice == "1":
        fixthecar()
    elif choice == "2":
        sellit()
    elif choice == "3":
        backtobed()

def fixthecar():
    print("you open the hood to see that your headers are cracked")#your headers is the part the engine for the exost
    print("1. get a new one -$200")
    print("2. sell the car and give up")
    choice_1 = input(">")

    if choice_1 == "1":
        global cash
        cash = 8800
        print (cash)
    elif choice_1 == "2":
        sellit()
    elif choice_1 == "return":
        start()
def sellit():#sell it
    print ("you sell the car what on")
    print ("1. facebook marketplace")
    print ("2. cragslist")
    print ("3. sell it back to a dellership") 
    print ("4. sell it to your freand")
    choice_2 = input (">")
    if choice_2 == '1':
        global cash
        cash = 11500
        print (cash)
        getnewcar()
    elif choice_2 == '2':
        print ("you dont sell it because who uses creaglist anymore")
        sellit()
    elif choice_2 == '3':
        print("you make no money cuz the dealer is closed")
        sellit()
    elif choice_2 == "return":
        start()
    elif choice_2 == '4':
        print ("they do not want you car")
        sellit()
def backtobed():
    print ('return to wake up')
    cheats= input(">")
    if cheats == "add":#bread
        print("to bad so sad take better care of your money")
        backtobed()
    elif cheats == 'return':
        start()
    else:
        print("be real man")
        backtobed()


def getnewcar():
    print ("get a new car")
    print ("Y/N")
    get = input (">")    

    if get == 'Y':
        print ("work in proges")
    elif get == 'N':
        print ("this is the first\n!!GOOD JOB!!\n:)\nending pls enter car at the bottom")
    else:
        print ("pls make shore that it is upperchase")

def dev():
    print("jump func 1-4")
    jump= input('>')
    if jump == '1':
        start()
    elif jump == '2':
        fixthecar()
    elif jump == '3':
        sellit()
    elif jump == '4':
        backtobed()
    elif jump == 'start':
        start()
    else:
        print ("not a command")
        dev()

if startcar == "TEST":
    dev()
else:
    start()


#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress
#work in progress

"""car here pls \/ :pls do not enter more then one if 2nd play tho if car is the same just put a multaplyer
exampal car.pontiac firebird 77X
.1


!!ONLY THE ONE YOU INPUT!!
"""

#get it done by friday