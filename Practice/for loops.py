for i in range (10, 0 -1):
    print(i)

My_list = [1, 3, 6, 76, 54, 23, 22, 23, 12, 31]
sum = 0
for num in My_list:
    sum = sum + num
print (sum)

small = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5,]
big = []
for num in small:
    big.append(num*num)

print (big)



my_string = input ("enter word\n>")
for char in my_string:
    if char in ['a', 'e', 'i', 'o', 'u']:
        num_vowels += 1


print (num_vowels)

user_num = input("enter an integer\n>")
try:
    user_num = int(user_num)
except:
    print ("not an integer")

for i in range(1, 10):
    print(str(user_num)+ " x " + str(i) + " = " + str(user_num*i))

names = ['jim', 'ethan', ' oliver', 'beau']
for name in names:
    print ("hello, " + name)