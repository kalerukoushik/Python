import random
import time


def findWord(story, word):
    
    pos = story.find(word)
    print(pos)
    print(story[pos:])
    return(story[pos+1:])


def stories():
    print("ONLINE LIBRARY")
    print("The stories in here:")
    ch = int(input("Select a story to read:1.Time\n2.Sherlock\n3.Summary of sherlock\n"))
    story1 = """Time travel is the concept of movement between certain points in time,
    analogous to movement between different points in space by an object or a person,
    typically using a hypothetical device known as a time machine.
    Time travel is a widely-recognized concept in philosophy and fiction.
    The idea of a time machine was popularized by H. G. Wells' 1895 novel The Time Machine.

    It is uncertain if time travel to the past is physically possible.
    Forward time travel, outside the usual sense of the perception of time,
    is an extensively-observed phenomenon and well-understood within the framework of special relativity and general relativity.
    However, making one body advance or delay more than a few milliseconds compared
    to another body is not feasible with current technology. As for backwards time travel,
    it is possible to find solutions in general relativity that allow for it,
    but the solutions require conditions that may not be physically possible.
    Traveling to an arbitrary point in spacetime has a very limited support in theoretical physics,
    and usually only connected with quantum mechanics or wormholes, also known as Einstein-Rosen bridges."""

    story2 = """The Adventures of Sherlock Holmes is a collection of twelve short stories by Arthur Conan Doyle,
    featuring his fictional detective Sherlock Holmes. It was first published on 14 October 1892; the individual
    stories had been serialised in The Strand Magazine between July 1891 and June 1892. The stories are not in
    chronological order, and the only characters common to all twelve are Holmes and Dr. Watson. The stories are
    related in first-person narrative from Watson's point of view.

    In general the stories in The Adventures of Sherlock Holmes identify, and try to correct, social injustices.
    Holmes is portrayed as offering a new, fairer sense of justice. The stories were well received, and boosted
    the subscriptions figures of The Strand Magazine, prompting Doyle to be able to demand more money for his
    next set of stories. The first story, "A Scandal in Bohemia", includes the character of Irene Adler, who,
    despite being featured only within this one story by Doyle, is a prominent character in modern Sherlock
    Holmes adaptations, generally as a love interest for Holmes. Doyle included four of the twelve stories from
    this collection in his twelve favourite Sherlock Holmes stories, picking "The Adventure of the Speckled Band"
    as his overall favourite.
    """
    story3 = """All of the stories within The Adventures of Sherlock Holmes are told in a first-person narrative
    from the point of view of Dr. Watson, as is the case for all but four of the Sherlock Holmes stories.[6] The
    Oxford Dictionary of National Biography entry for Doyle suggests that the short stories contained in The
    Adventures of Sherlock Holmes tend to point out social injustices, such as "a king's betrayal of an opera
    singer, a stepfather's deception of his ward as a fictitious lover, an aristocratic crook's exploitation of
    a failing pawnbroker, a beggar's extensive estate in Kent."[1] It suggests that, in contrast, Holmes is portrayed
    as offering a fresh and fair approach in an unjust world of "official incompetence and aristocratic privilege".[1]
    The Adventures of Sherlock Holmes contains many of Doyle's favourite Sherlock Holmes stories. In 1927, he submitted
    a list of what he believed were his twelve best Sherlock Holmes stories to The Strand Magazine. Among those he listed
    were "The Adventure of the Speckled Band" (as his favourite), "The Red-Headed League" (second), "A Scandal in Bohemia"
    (fifth) and "The Five Orange Pips" (seventh).[7] The book was banned in the Soviet Union in 1929 because of its alleged
    "occultism",[8] but the book gained popularity in a black market of similarly banned books, and the restriction was lifted in 1940"""

    story = [story1, story2, story3]
    if(ch == 1):
        print(story[0])
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
    elif(ch == 2):
        print(story[1])
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
    elif(ch == 3):
        print(story[2])
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

    print("Happy reading!")




def clothing():
    shop = ['Men', 'Women', 'Kids', 'Foot', 'Ladies purse']
    men = [['item1','item2','item3','item4','item5'], [1000, 2000, 1500, 2500, 2200]]
    women = [['womenItem1','womenItem2','womenItem3','womenItem4','womenItem5'], [1000, 2000, 1500, 2500, 2200]]
    kids =[['kidsItem1','kidsItem2','kidsItem3','kidsItem4','kidsItem5'], [2300, 1900, 2100, 2500, 3200]]
    foot = [['footItem1','footItem2','footItem3','footItem4','footItem5'], [ 1500, 2500, 2200, 2300, 1900]]
    ladies_purse = [['LadiesPurse1','LadiesPurse2','LadiesPurse3','LadiesPurse4','LadiesPurse5'], [2000, 1500, 2500, 2200, 1900]]

    print("WELCOME TO MYSHOP")
    print("1.",shop[0], "\n2.",shop[1], "\n3.",shop[2], "\n4.",shop[3], "\n5.",shop[4])
    item = int(input("Select which item do u want purchase:"))

    if(item == 1):
        print(men[0][0],":", men[1][0])
        print(men[0][1],":", men[1][1])
        print(men[0][2],":", men[1][2])
        print(men[0][3],":", men[1][3])
        print(men[0][4],":", men[1][4])
        no = int(input("Enter the no of items u want to select:"))
        cost = 0
        for i in range(0, no):
            item_no = int(input("select item no:"))
            cost = cost + men[1][item_no-1]
        print(cost)

    elif(item == 2):
        print(women[0][0],":", women[1][0])
        print(women[0][1],":", women[1][1])
        print(women[0][2],":", women[1][2])
        print(women[0][3],":", women[1][3])
        print(women[0][4],":", women[1][4])
        no = int(input("Enter the no of items u want to select:"))
        cost = 0
        for i in range(0, no):
            item_no = int(input("select item no:"))
            cost = cost + women[1][item_no-1]
        print(cost)

    elif(item == 3):
        
        print(kids[0][0],":", kids[1][0])
        print(kids[0][1],":", kids[1][1])
        print(kids[0][2],":", kids[1][2])
        print(kids[0][3],":", kids[1][3])
        print(kids[0][4],":", kids[1][4])
        no = int(input("Enter the no of items u want to select:"))
        cost = 0
        for i in range(0, no):
            item_no = int(input("select item no:"))
            cost = cost + kids[1][item_no-1]
        print(cost)

        
    elif(item == 4):
        
        print(foot[0][0],":", foot[1][0])
        print(foot[0][1],":", foot[1][1])
        print(foot[0][2],":", foot[1][2])
        print(foot[0][3],":", foot[1][3])
        print(foot[0][4],":", foot[1][4])
        no = int(input("Enter the no of items u want to select:"))
        cost = 0
        for i in range(0, no):
            item_no = int(input("select item no:"))
            cost = cost + foot[1][item_no-1]
        print(cost)

    elif(item == 5):

        print(ladies_purse[0][0],":", ladies_purse[1][0])
        print(ladies_purse[0][1],":", ladies_purse[1][1])
        print(ladies_purse[0][2],":", ladies_purse[1][2])
        print(ladies_purse[0][3],":", ladies_purse[1][3])
        print(ladies_purse[0][4],":", ladies_purse[1][4])
        no = int(input("Enter the no of items u want to select:"))
        cost = 0
        for i in range(0, no):
            item_no = int(input("select item no:"))
            cost = cost + ladies_purse[1][item_no-1]
        print(cost)

    else:
        print("Select correctly!")

    print("\nPAYMENT")
    print("1.Cash on delivery")
    print("2.PayTM")

    payment = int(input("Enter the mode of payment:"))
    if(payment == 1):
        print("Your order(s) will receive shortly")
    elif(payment == 2):
        print("Page will be redirected to PayTM")




def mobile():
    print("MOBILES")
    print("shop by brand")
    print("1.Micromax\n")
    print("2.Redmi\n")
    print("3.Vivo\n")
    ch=int(input("select ur brand"))
    at = 0
    if(ch==1):
        print("MICROMAX")
        l=[['1.micromax doodle','2.micromax canvas 2','3.micromax note 7','4.micromax note 6'],['','','','']]
        print(l[0][0]+'\t'+l[0][1]+'\t'+l[0][2]+'\t'+l[0][3])
        s=[6866,7836,7536,6787]
        d=int(input("select your model"))
        if(d<=10):
            print(l[0][d-1])
            at=at+s[d-1]
            print(s[d-1])
        else:
            print("invalid selection")
    elif(ch==2):
        print("REDMI")
        l=[['1.mi a1','2.mi note 6 pro','3.mi note 7','4.mi note 6'],['','','','']]
        print(l[0][0]+'\t'+l[0][1]+'\t'+l[0][2]+'\t'+l[0][3])
        s=[6866,7836,7326,6787]
        d=int(input("select your model"))
        if(d<=10):
            print(l[0][d-1])
            at=at+s[d-1]
            print(s[d-1])
        else:
            print("invalid selection")
    elif(ch==3):
        print("VIVO")
        l=[['1.vivo v11 pro','2.vivo v15 pro','3.vivo  v7','4.vivo v9'],['','','','']]
        print(l[0][0]+'\t'+l[0][1]+'\t'+l[0][2]+'\t'+l[0][3])
        s=[6866,7836,736,6787]
        d=int(input("select your model"))
        if(d<=10):
            print(l[0][d-1])
            at=at+s[d-1]
            print(s[d-1])
        else:
            print("invalid selection")     




    
def shopping():
    print("\nShopping ")
    sh = int(input("Select from the below:\n1.Clothing\n2.Mobile\n"))
    if(sh == 1):
        clothing()
        ch = str(input("Do u want to shop clothes again:(Y|N)"))
        if(ch == 'Y' or ch =='y'):
            shopping()
        else:
            print("Thank you!! Visit again.")

    elif(sh == 2):
        mobile()
        ch1 = str(input("Do u want to shop mobiles again:(Y|N)"))
        if(ch1 == 'Y' or ch1 =='y'):
            shopping()
        else:
            print("Thank you!! Visit again.")
        
        



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

    players = int(input("Enter the no of players:"))
    n = 0
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
                time.sleep(0.1)
                
                i = i + 1
            print()
            
            j = j+1
        winner = str(input("Enter the winner:"))
        print("Congrats",winner)
    else:
        print("Ok Bye")
        



def mgmt():
    ch = int(input("\n\nSelect to view\n 1.Faculty\n2.Student\n3.Shopping\n4.Online Library\n"))
    faculty = ['KT', 'KK', 'SK', 'DD', 'JMKS']
    student = ['KT', 'KK', 'SK', 'DD', 'JMKS']
    if(ch == 1):
        print("Faculty list : ", faculty)
        fac = input("Select faculty:")
        if(fac == 'KT'):
            print("Salary : 100000")
            print("Leaves : 0")
            print("Subjects: MLPR")
            print("Designation: Associate Professor")
            print("Experience : 5 Years")
            print("Date of joining : 11-01-2014")
            print("Transfer : Himalayas")
        elif(fac == 'KK'):
            print("Salary : 100000")
            print("Leaves : 0")
            print("Subjects: ADS")
            print("Designation:  Professor")
            print("Experience : 3 Years")
            print("Date of joining : 11-01-2015")
            print("Transfer : NO")
        elif(fac == 'SK'):
            print("Salary : 100000")
            print("Leaves : 0")
            print("Subjects: DWDM")
            print("Designation: Assistant Professor")
            print("Experience : 4 Years")
            print("Date of joining : 11-01-2014")
            print("Transfer : NO")
        elif(fac == 'DD'):
            print("Salary : 100000")
            print("Leaves : 0")
            print("Subjects: DBMS")
            print("Designation: HOD")
            print("Experience : 7 Years")
            print("Date of joining : 11-01-2011")
            print("Transfer : NO")
        elif(fac == 'JMKS'):
            print("Salary : 100000")
            print("Leaves : 0")
            print("Subjects: OS")
            print("Designation: Lab Faculty")
            print("Experience : 2 Years")
            print("Date of joining : 11-01-2018")
            print("Transfer : NO")
        else:
            print("Faculty record not found!!")
    elif(ch == 2):
        print("Students:", student)
        std = input("Select student")
        if(std == 'KT'):
            print("Roll No: 165B6")
            print("Migration: Sri Indu")
            print("Attendence : 99.3")
            print("Fee due : 90,000(hostel)")
            print("Department : CSE")
            print("Nationality : Indian")
        elif(std == 'KK'):
            print("Roll No: 165B7")
            print("Migration: No")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Nepal")
        elif(std == 'SK'):
            print("Roll No: 165B8")
            print("Migration: No")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Sudan")
        elif(std == 'DD'):
            print("Roll No: 17513")
            print("Migration: No")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Sri Lanka")
        elif(std == 'JMKS'):
            print("Roll No: 165A1")
            print("Migration: No")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Dubai")
        else:
            print("No student record ")
    elif(ch == 3):
        shopping()
    elif(ch == 4):
        stories()
    ch1 = str(input("Do you want to continue:(Y|N):"))
    if(ch1 == 'Y' or ch1 == 'y'):
        mgmt()
    else:
        print("Thank you !! Visit Again")
    exit()
            
            
        
def faculty():
    ch = int(input("Select to view\n 1.My details\n2.Student\n3.Shopping\n4.Online Library\n"))
    student = ['KT', 'KK', 'SK', 'DD', 'JMKS']
    if(ch == 1):
        print("Salary : 100000")
        print("Leaves : 0")
        print("Subjects: DBMS")
        print("Designation: HOD")
        print("Experience : 7 Years")
        print("Date of joining : 11-01-2011")
    elif(ch == 2):
        print("Students:", student)
        std = input("Select student")
        if(std == 'KT'):
            print("Roll No: 165B6")
            print("Attendence : 99.3")
            print("Fee due : 90,000(hostel)")
            print("Department : CSE")
            print("Nationality : India")
        elif(std == 'KK'):
            print("Roll No: 165B7")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Nepal")
        elif(std == 'SK'):
            print("Roll No: 165B8")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Sudan")
        elif(std == 'DD'):
            print("Roll No: 17513")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Sri Lanka")
        elif(std == 'JMKS'):
            print("Roll No: 165A1")
            print("Attendence : 90")
            print("Fee due : -Nil-")
            print("Department : CSE")
            print("Nationality : Dubai")
        else:
            print("No student record ")
    elif(ch == 3):
        shopping()
    elif(ch == 4):
        stories()
    ch1 = str(input("Do you want to continue:(Y|N):"))
    if(ch1 == 'Y' or ch1 == 'y'):
        faculty()
    else:
        print("Thank you !! Visit Again")
    
    exit()
     

        
def std():
    faculty = ['KT', 'KK', 'SK', 'DD', 'JMKS']
    trainers = ['Lavish Arora', 'Srikanth', 'Santhosh']
    ch = int(input("Select choice:\n1.Request Trainer\n2.My Details\n3.Game(Tambola)\n4.Shopping\n5.Online Library\n"))
    if(ch == 1):
        print("The Trainings available are : \n1.Python\n2.Java\n3.Ruby\n")
        tra = int(input("Select your preferred training:"))
        if(tra == 1):
            print("The trainers available are:")
            print("1.",trainers[0],"\n Professional in Python, and done a lot of algorithms under Machine Learning")
            print("2.",trainers[1],"\n Professional in Python")
            print("3.",trainers[2],"\n Professional in Python")
            trainer = int(input("\nSelect a trainer:"))
            if(trainer == 1):
                print(trainers[0])
                print("Status:   Currently available ")
                sel = str(input("Do you want to select : (Y|N)"))
                if(sel == 'Y' or sel == 'y'):
                    print("trainer",trainers[0]," selected")
                    print("And we will let you know within 24 hours, about ", trainers[0],'\'s' " visit")
                else:
                    print("Thank you")
            elif(trainer == 2):
                print(trainers[1])
                print("Status:   Currently unavailable")
                print("Will be free after 1 month ")
                
    elif(ch == 2):
        
        print("Your details:")
        print("Roll No: 165B8")
        print("Attendence : 90")
        print("Fee due : -Nil-")
        print("Department : CSE")
        print("Nationality : Dubai")

    elif(ch == 3):
        game()
        ch = str(input("Do u want to play again(Y|N):"))
        if(ch == 'Y' or ch == 'y'):
                game()
        else:
            print("thank you visit again!!")
    elif(ch == 4):
        shopping()
    elif(ch == 5):
        stories()
        ch2 = str(input("Do you want to read another story:(Y|N):"))
        if(ch2 == 'Y' or ch2 == 'y'):
            stories()
        else:
            print("Tq visit again")
    ch1 = str(input("Do you want to continue:(Y|N):"))
    if(ch1 == 'Y' or ch1 == 'y'):
        std()
    else:
        print("Thank you !! Visit Again")
    exit

    
    
    

print("GuruNanak Institutions")
mgmtID = "mgmt1"
empID = "emp1"
stdID = "std1"
id = str(input("Enter Mgmt ID/ Emp ID/ Std ID:"))
if(id == mgmtID):
    mgmt()
        
elif(id == empID):
    faculty()
        
elif(id == stdID):
    std()
        
else:
    print("Wrong Id!!") 
