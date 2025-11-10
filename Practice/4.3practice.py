#while condition:
#   do somthing

num = 0
continue_adding = True


while continue_adding == True:
    num += 1
    print(num)
    ask = input ("whould you to go on Y/N\n>")
    if ask.lower == 'n':
        continue_adding = False