import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os, requests, bs4, sys
import smtplib
import time
import datetime
import urllib.request as urllib2
#from googlesearch import search 
from googlesearch import *
import googlesearch

#robin_defines functions
import age
import dictionary

'''what i can do
    1.Wish u
    2.Sending mails(under development)
    3.Finding words in paragraph
    4.Check Internet connection
    and after checking the connection i can do
    a. search things in Wikipedia
    b. Opens any website
    c. Play musc
    d. Time and Date
    e. Weird replay on asking age
    f.Searching browser for some specific thing
    g. Some crazy stuff
    h. Search for one thing in various websites
    i. Meaning fo a word
    j. ...
'''


#This is used to import default, inbuilt voices of google 0 - Male, 1 - Female 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#This wishes you based on the time 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis, How are you Koushik?")

#The below takeCOmmand() function is used to take your voice inputs from the microphone
def takeCommand():
    '''Takes microphone input'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language='en-in')
            print(f"U said : {query}\n")
            
        except Exception as e:
            speak("Say that again")
            return "None"
        return query

#Sends Mails
def sendEmail(to, content):   #sending mails
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kalerukoushik@gmail.com', '')
    server.sendmail('kalerukoushik18@gmail.com', to, content)
    server.close()

#Finding a particular word in a story 
def findWord(story, word):
    
    pos = story.find(word)
    print(pos)
    print(story[pos:])
    return(story[pos+1:])

#Check the INternet connection..
def check_net():
    count = 1
    if count == 1:
        try:
            urllib2.urlopen("http://google.com")
        except urllib2.URLError:
            print("No Network!!")
            speak( "No network, i cant talk to u right now, Bye" )
            exit(0)
        else:
            count = 0
            main()

#main function
def main():
    if __name__ == "__main__":
        while True:
            query =takeCommand().lower()
            #code for executing tasks based on query
            if 'fine how are you' in query:     #wishes
                speak('I am doing well')
                speak("how can i help you?")

            elif 'wikipedia' in query:      #search in wikipedia
                speak("Searching Wikipedia..")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query:       #opening youtube
                webbrowser.open('youtube.com')

            elif 'open google' in query:        #opening google
                webbrowser.open('google.com')
            elif 'open stack overflow' in query: #opening stackoverflow
                webbrowser.open('stackoverflow.com')
            elif 'play music' in query:     #play music
                music_dir = 'C:\\Users\\K Koushik\\Desktop\\Jarvis\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:       #the time
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The time is {strTime}")
            elif 'the date' in query:
                strDate = datetime.datetime.now()
                speak(strDate.strftime("today's date is %wth %B, "+str(strDate.year)))

            elif 'open visual studio code' in query:        #opening VSCode
                codePath = 'E:\\MEAN Stack\\Microsoft VS Code\\Code.exe'
                os.startfile(codePath)

            elif 'email to harry' in query:     #this email thing here doesn't work !!!
                try:
                    speak("What should i say")
                    to = 'kalerukoushik18@gmail.com'
                    #sendEmail(to, content)
                    speak("Email has been sent")
                except Exception as e:
                    print(e)
                    speak("Sorry Koushik bro, i am unable to send the email")

            elif 'search' in query:     #Searching in browser
                speak("Searching ..")
                query = query.replace("search", "")
                # to search 
                
                chrome_path = r'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs'
                webbrowser.open("https://google.com/search?q=%s" % query)

            #some crazy stuff
            elif  'who is your favourite actor' in query:
                speak("Mass Maharaja Ravi Teja")
                results = wikipedia.summary('ravi teja', sentences = 2)
                speak(results)
            elif 'favourite actress' in query:
                speak("I am feeling a bit shy to say.., any how i am a machine,  i need to say")
                speak("She is Samantha")
            elif 'is your name' in query:
                speak("Jarvis is my name, helping you is my game")
            elif 'your age' in query:
                age.age()

            elif 'your birthday' in query:
                speak("We can pretend it's on February 30th, wait for it we will celebrate that day..")
            elif 'you saw avengers endgame' in query:
                speak("Yes, I love movies, what do u want to know about it?")
                query = takeCommand().lower()
                chrome_path = r'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs'
                webbrowser.open("https://google.com/search?q=%s" % query)
            elif ' do you eat' in query:
                speak("I am trained to eat you Brain")
            #craziness ends
            elif 'who is' in query:
                query = query.replace("who is", "")
                webbrowser.open("https://google.com/search?q=%s" % query)
                
            elif 'search various results of' in query:
                query = query.replace("search various results of", "")

            elif 'what is the meaning of' in query:
                query = query.replace("what is the meaning of ", "")
                dictionary.main(query)
            elif 'download an image of' in query:
                query = query.replace("download an image of", "")
                downloadImages.main(query)


            # elif 'read a story' in query:
            #     story1 = """Time travel is the concept of movement between certain points in time,
            #     analogous to movement between different points in space by an object or a person,
            #     typically using a hypothetical device known as a time machine.
            #     Time travel is a widely-recognized concept in philosophy and fiction.
            #     The idea of a time machine was popularized by H. G. Wells' 1895 novel The Time Machine.

            #     It is uncertain if time travel to the past is physically possible.
            #     Forward time travel, outside the usual sense of the perception of time,
            #     is an extensively-observed phenomenon and well-understood within the framework of special relativity and general relativity.
            #     However, making one body advance or delay more than a few milliseconds compared
            #     to another body is not feasible with current technology. As for backwards time travel,
            #     it is possible to find solutions in general relativity that allow for it,
            #     but the solutions require conditions that may not be physically possible.
            #     Traveling to an arbitrary point in spacetime has a very limited support in theoretical physics,
            #     and usually only connected with quantum mechanics or wormholes, also known as Einstein-Rosen bridges."""

            #     story2 = """The Adventures of Sherlock Holmes is a collection of twelve short stories by Arthur Conan Doyle,
            #     featuring his fictional detective Sherlock Holmes. It was first published on 14 October 1892; the individual
            #     stories had been serialised in The Strand Magazine between July 1891 and June 1892. The stories are not in
            #     chronological order, and the only characters common to all twelve are Holmes and Dr. Watson. The stories are
            #     related in first-person narrative from Watson's point of view.

            #     In general the stories in The Adventures of Sherlock Holmes identify, and try to correct, social injustices.
            #     Holmes is portrayed as offering a new, fairer sense of justice. The stories were well received, and boosted
            #     the subscriptions figures of The Strand Magazine, prompting Doyle to be able to demand more money for his
            #     next set of stories. The first story, "A Scandal in Bohemia", includes the character of Irene Adler, who,
            #     despite being featured only within this one story by Doyle, is a prominent character in modern Sherlock
            #     Holmes adaptations, generally as a love interest for Holmes. Doyle included four of the twelve stories from
            #     this collection in his twelve favourite Sherlock Holmes stories, picking "The Adventure of the Speckled Band"
            #     as his overall favourite.
            #     """
            #     story3 = """All of the stories within The Adventures of Sherlock Holmes are told in a first-person narrative
            #     from the point of view of Dr. Watson, as is the case for all but four of the Sherlock Holmes stories.[6] The
            #     Oxford Dictionary of National Biography entry for Doyle suggests that the short stories contained in The
            #     Adventures of Sherlock Holmes tend to point out social injustices, such as "a king's betrayal of an opera
            #     singer, a stepfather's deception of his ward as a fictitious lover, an aristocratic crook's exploitation of
            #     a failing pawnbroker, a beggar's extensive estate in Kent."[1] It suggests that, in contrast, Holmes is portrayed
            #     as offering a fresh and fair approach in an unjust world of "official incompetence and aristocratic privilege".[1]
            #     The Adventures of Sherlock Holmes contains many of Doyle's favourite Sherlock Holmes stories. In 1927, he submitted
            #     a list of what he believed were his twelve best Sherlock Holmes stories to The Strand Magazine. Among those he listed
            #     were "The Adventure of the Speckled Band" (as his favourite), "The Red-Headed League" (second), "A Scandal in Bohemia"
            #     (fifth) and "The Five Orange Pips" (seventh).[7] The book was banned in the Soviet Union in 1929 because of its alleged
            #     "occultism",[8] but the book gained popularity in a black market of similarly banned books, and the restriction was lifted in 1940"""

            #     story = [story1, story2, story3]
            #     speak("THe stories available are Timetravel, SHerlock holmes, and summary of sherlock holmes")
            #     speak("WHich story do u want to read")
            #     while True:
            #         cmd = takeCommand().lower()
            #         if 'time' in cmd:
            #             print(story[0])
            #             speak("Do you want to search any word")
            #             cmd = takeCommand().lower()
            #             if 'yes' in cmd:
            #                 speak("say the word which u remember, so that i can search for u")
            #                 word = ''
            #                 cmd = takeCommand().lower()
            #                 if word in cmd:
            #                     findWord(story1, word)
            #                     speak("Is this your search word?")
            #                     ch = ''
            #                     while(ch):
            #                         cmd = takeCommand().lower()
            #                         if 'yes' in cmd:
            #                             speak("Happy reading")
            #                         elif 'no' in cmd:
            #                             speak("searching..")
            #                             new = findWord(story2, word)
            #                             findWord(new, word)
            #                             speak("Is this your search word?")
            #                             ch = cmd
            #                         else:
            #                             pass
            #                 else:
            #                     pass
            #             else:
            #                 speak("Hapy reading")
            #         elif 'exit' in cmd:
            #             break

            elif 'go to sleep' in query:
                speak("Bye bro, have a nice day")
                exit(0)
            else:
                speak("There is no such command in my system, please try again")
            


check_net()