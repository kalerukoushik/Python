import jarvis
import time
def findWord(story, word):
    
    pos = story.find(word)
    print(pos)
    print(story[pos:])
    return(story[pos+1:])

def tell_story():
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
    jarvis.speak("THe stories available are Timetravel, SHerlock holmes, and summary of sherlock holmes")
    jarvis.speak("WHich story do u want to read")
    while True:
        query =jarvis.takeCommand().lower()
        if 'time' in query:
            print(story[0])
            jarvis.speak("Do you want to search any word")
            if 'yes' in query:
                jarvis.speak("say the word which u remember, so that i can search for u")
                word = ''
                if word in query:
                    findWord(story1, word)
                    jarvis.speak("Is this your search word?")
                    ch = ''
                    while(ch):
                        if 'yes' in query:
                            jarvis.speak("Happy reading")
                        elif 'no' in query:
                            jarvis.speak("searching..")
                            new = findWord(story2, word)
                            findWord(new, word)
                            jarvis.speak("Is this your search word?")
                            ch = jarvis.takeCommand()
                        else:
                            pass
                else:
                    pass
            else:
                jarvis.speak("Happy reading")
                time.sleep(10)
                
            
            
    