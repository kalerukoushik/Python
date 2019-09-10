    story = [story1, story2, story3]
    if(ch == 1):
        print(story[0])
        readYN = str(input("Do you want to read the story:(Y|N)"))
        if(readYN == 'Y' or readYN == 'y'):
            
            word = str(input("Enter the word that you want to find:"))
            findWord(story1, word)
            ch = str(input("\nIs this your search word:(Y|N)"))
            while(ch):
                if(ch == 'Y' or ch == 'y'):
                    break
                else:
                    new = findWord(story1, word)
                    findWord(new, word)
                    ch = str(input("\nIs this your search word:(Y|N)"))
        else:
            std()
            
    elif(ch == 2):
        print(story[1])
        readYN = str(input("Do you want to read the story:(Y|N)"))
        if(readYN == 'Y' or readYN == 'y'):
            word = str(input("Enter the word that you want to find:"))
            findWord(story2, word)
            ch = str(input("\nIs this your search word:(Y|N)"))
            while(ch):
                if(ch == 'Y' or ch == 'y'):
                    break
                else:
                    new = findWord(story2, word)
                    findWord(new, word)
                    ch = str(input("\nIs this your search word:(Y|N)"))
        else:
            std()
    elif(ch == 3):
        print(story[2])
        readYN = str(input("Do you want to read the story:(Y|N)"))
        if(readYN == 'Y' or readYN == 'y'):
            word = str(input("Enter the word that you want to find:"))
            findWord(story3, word)
            ch = str(input("\nIs this your search word:(Y|N)"))
            while(ch):
                if(ch == 'Y' or ch == 'y'):
                    break
                else:
                    new = findWord(story3, word)
                    findWord(new, word)
                    ch = str(input("\nIs this your search word:(Y|N)"))
        else:
            std()
