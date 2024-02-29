import random

# Mona Achaaoud

def Choices():

    try:
        Choices.x = int(input("Rock=1, Paper=2, Scissors=3\n"))
    except ValueError:
        print("Number must be between 1-3")
        Choices()

    random_Choices = [1, 2, 3]
    Choices.y = random.choice(random_Choices)


def Game(x, y):

    if(type(x) != int or x > 3):
        return "Number must be between 1-3"
        Choices()
        Game(Choices.x, Choices.y)
    else:
        z = x - y
        if (x == y):
            return "Tie"
        elif (z == 1 or z == -2):
            return "You win"
        else:
            return "You loose"


if __name__ == '__main__':
   Choices()
   Game(Choices.x, Choices.y)