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
    tables = [t1, t2, t3, t4, t5, t6, t7, t8, t9]

    players = int(input("\nEnter the no of players(min 2 players):"))
    n = 0
    if(players == 1):
        print("Sorry !!! 1 player can't play this game\n")
        game()
    else:
        while n < players and players < 11:
            random.shuffle(t1)
            random.shuffle(t2)
            random.shuffle(t3)
            random.shuffle(t4)
            random.shuffle(t5)
            random.shuffle(t6)
            random.shuffle(t7)
            random.shuffle(t8)
            random.shuffle(t9)
            random.shuffle(tables)
            print("User",n+1,":", tables[n])
            n = n+1
            print()

        
        print("Plz note down the tables")
        ch = str(input("\nShall we start the game:(Y|N)"))

        if( ch == 'Y' or ch == 'y'):
            i = 1
            j = 1
            while(j < players+1):
                while(i < 10 * players+1):
                    print("User:")
                    j = j + 1
                    print(random.randint(1,91),"\n")
                    time.sleep(1)
                    i = i + 1
                print()
                
                j = j+1
            winner = str(input("Enter the winner:"))
            print("*****Congrats",winner,"****")
        else:
            print("Ok Bye")
            
game()

ch = str(input("Do u want to play again(Y|N):"))
if(ch == 'Y' or ch == 'y'):
        game()
else:
    print("thank you visit again")




#new

    
    
