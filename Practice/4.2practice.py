import random

games = ["minecraft", "ultrakill", "space enginner", "jedi fallen order", "battlefield 6"]
for game in games:
    print (game)
number = [1,2,3,4,5]
for num in number:
    print (num)
    for i in range (0,5):
        print ('rank' + str(i) +": " + games [i])
#print every number from 1 - 5 using a for loop


for i in range (0,100,10):
    print (i)


random_numbers = []
for i in range (0,100):
    random_numbers.append (random.randint(-100,101))


for i in range (0, len(random_numbers)):
    if random_numbers[i] < 0:
        random_numbers.pop(i)