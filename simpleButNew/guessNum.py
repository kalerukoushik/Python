import random
print("*** GUESS THE NUMBER ***\n")
n = 20
original_num = int(n * random.random())+1
#print(original_num)
guess = 0
while guess != original_num:
    guess = int(input("Guess a number:"))
    if( guess > original_num ):
        print(guess, "is bigger than original number" )

    elif( guess < original_num ):
        print(guess, "is smaller than original number" )

print("\n\nCongrats the original number is :",guess)
