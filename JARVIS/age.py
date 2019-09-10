import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os, requests, bs4, sys
import smtplib
import time
import datetime
from datetime import *
import jarvis
def age():
    jarvis.speak("You know it's rude to ask an assistant their age")
    jarvis.speak("Any how..") 
    dob = "01/05/2019"
    dob = datetime.strptime(dob, '%d/%m/%Y')
    jarvis.speak("Here are your age statistics...")
    jarvis.speak ("%d Years or" % ((datetime.today() - dob).days/365))
    jarvis.speak ("%d Months or" % ((datetime.today() - dob).days/30))
    jarvis.speak ("%d Days or" % ((datetime.today() - dob).days*24))
    jarvis.speak ("%d Minutes or" % ((datetime.today() - dob).days*1440))
    jarvis.speak ("%d Seconds or" % ((datetime.today() - dob).days*86400))
    jarvis.speak("Ohh God it's damn big to calculate")
    jarvis.speak("I think you are satisfied with my age")
