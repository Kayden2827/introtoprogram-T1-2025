def start ():
    print("you wake up to your car is broken")
    def choice1():
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
        choice1()

def fixthecar():
    print("you open the hood to see that your headers are cracked")
def sellit():
    print ("you sell the car what on")
    print ("1. facebook marketplace")
    print ("2. cragslist")
    print ("3. sell it back to a dellership") 
def backtobed():
    start()
    

start()