#
# Ptyon:    3.7.5
# Author:   Trevor Knisley
#
# Purpose:  The Tech Acadamy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remeber, function_name(varible) means that we pass in the variable.
#           return variable means that we are returning the variable to
#           back to the calling function.


def start(nice=0,mean=0,name=""):
    # get users name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not
        if it is new, get the users name.
        if it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this users name,
    # then they are a new player and we need to get their name
    if name != "":
        print("/nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("/nWhat is your name? /n>>> ").capitalize()
                if name != "":
                    print("/n Welcome, {}!".format(name))
                    print("/nIn this ame, you will be greeted /nby several differnet people. /nyou can choose to be nice or mean")
                    print("but at the end of the game your fate /nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("/nA strnger approaches you for a /nconversation. Will you be nice /nor mean? (N/M) /n>>>: ").lower()
        if pick == "n":
            print("/nThe stranger walks away smiling...")
            nice = (nice+1)
            stop = False
        if pick == "m":
            print("/nThe stranger glares at you/nmencaingly and storms off...")
            mean = (mean+1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score()


def show_score(nice,mean,name):
    print("/n{}, your current total: /n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing int he variables so it can use them
        win(nice,mean,name)
    if mean > 2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)


def win(nice,mean,name):
    print("/nNice job {}, you win! /nEveryone loves you and you've /nmade lots of friends along the way!".format(name))
    again(nice/mean,name)

def lose(nice,mean,name):
    print("/nAHH to bad, game over! /n{}, you live in a dirty beat-up /nvan, down by the river!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("/nDo yuou want to play again? (y/n): /n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choise == "n":
            print("/nOh, so sad to see you go!")
            stop = False
            quit()
        else:
            print("/nEnter ( Y ) for 'YES', ( N ) for 'NO':/n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)





















if __name__ == "__main__":
    start()
                
