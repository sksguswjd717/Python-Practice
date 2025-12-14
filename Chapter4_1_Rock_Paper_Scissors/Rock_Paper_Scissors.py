import random

player = 0
computer = random.randint(1,3)
# print(x)


print("===================\n")
print("Rock Paper Scissors\n")
print("===================\n")

print("1) ✊")
print("2) ✋")
print("3) ✌️")
player = int(input("Pick a number : "))

print("\n")

if player == 1:
    print("You chose: ✊")
elif player == 2:
    print("You chose: ✋")
else:
    print("You chose: ✌️")

if computer == 1:
    print("CPU chose: ✊\n")
elif computer == 2:
    print("CPU chose: ✋\n")
else:
    print("CPU chose: ✌️\n")

if player == 1: # player rock
    if computer == 1:#computer rock
        print("Draw!")
    elif computer == 2:#computer paper
        print("You lost")
    else :
        print("The player won!")
elif player == 2: # player paper
    if computer == 1:#computer rock
        print("The player won!")
    elif computer == 2:#computer paper
        print("Draw!")
    else :              #computer scissors
        print("You lost")
else: # player scissors
    if computer == 1:#computer rock
        print("You lost")
    elif computer == 2:#computer paper
        print("The player won!")
    else :              #computer scissors
        print("Draw!")