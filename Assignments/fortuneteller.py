import random
def fortune_cookie ():
    age = input ("how old are you\n>")
    felling =  input ("how are you\n>")
    game = input ("what is your favorite game\n>")


    fortune = ('you will find what you are loking for', 'something good will happen soon', 'you will have a good time', 'do not eat the fortune eat the cookie', 'you will find your day' )
    print(random.choice(fortune))

fortune_cookie()
