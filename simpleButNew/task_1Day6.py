import random
import time
def game():
    t1 = [1, 11, 21, 31, 41, 51, 61, 71, 81]
    t2 = [2, 12, 22, 32, 42, 52, 62, 72, 82]
    t3 = [3, 13, 23, 33, 43, 53, 63, 73, 83]
    t4 = [4, 14, 24, 34, 44, 54, 64, 74, 84]
    t5 = [5, 15, 25, 35, 45, 55, 65, 75, 85]
    t6 = [6, 16, 26, 36, 46, 56, 66, 76, 86]
    t7 = [7, 17, 27, 37, 47, 57, 67, 77, 87]
    t8 = [8, 18, 28, 38, 48, 58, 68, 78, 88]
    t9 = [9, 19, 29, 39, 49, 59, 69, 79, 89]


    players = int(input("Enter the no of players:"))

    

    random.shuffle(t1)
    print(t1)

    random.shuffle(t2)
    print(t2)

    print("Plz note down the tables")
    ch = str(input("\nShall we start the game:(Y|N)"))

    if( ch == 'Y' or ch == 'y'):
        j = 1
        while(j < 11):
            print("User 1 :")
            print(random.randint(1,101))
            time.sleep(0.1)
            print("User 2 :")
            print(random.randrange(1, 101))
            time.sleep(0.1)
            print()
            j = j+1
        winner = str(input("Enter the winner:"))
        print("Congrats",winner)
    else:
        print("Ok Bye")
        
game()

ch = str(input("Do u want to play again(Y|N):"))
if(ch == 'Y' or ch == 'y'):
        game()
else:
    print("thank you visit again")




#new

    
    
