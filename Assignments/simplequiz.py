a1 = input ("who is luke skywalkers father\n>")
a2 = input ("who is darth vaders second kid\n>")
a3 = input ("who is darth vader\n>")
a4 = input ("where was the obi won and anikin fight happened\n>")
a5 = input ('complete the "quote no luke im your ____"\n>')

def calculater():
    score = 0

    if a1.lower == "darth vader":
        score = score + 1

    elif a2.lower == "princess Leia":
        score = score + 1

    elif a3.lower == "anakin skywalker":
        score = score + 1

    elif a4.lower == "mustafar":
        score = score + 1

    elif a5 == "father":
        score = score + 1
    else:
        print('stop')

    print("score " + str(score) + "/5")

calculater()
