cat = input("input wind speed\n>")



if int(cat) < 74:
    print("this is a tropical storm")

elif int(cat) < 96:
    print("that is a category 1")

elif int(cat) < 111:
    print ("that is a category 2")

elif int(cat) < 130:
    print("that is a catagory 3")

elif int(cat) < 157:
    print("that is a catagory 4")

elif int(cat) >= 157:
    print ("that is a catagoty 5")

else:
    print("input an intager")
