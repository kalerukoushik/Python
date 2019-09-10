from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition
from nltk.corpus import wordnet
from kivy.uix.image import Image
import random
from kivy.core.window import Window
from kivy.uix.layout import *
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.properties import  ObjectProperty

RootApp = None

class ScreenZero(Screen):
    pass
class Who(Screen):  #screen1
    pass

class LoginOrRegMgmt(Screen):
    pass

class LoginOrRegFac(Screen):
    pass
class RegFac(Screen):
    pass
class LoginOrRegStd(Screen):
    pass
class RegStd(Screen):
    pass

class MgmtHome(Screen):
    pass
class FacDetM(Screen):
    pass
class StdDetM(Screen):
    pass

class FacHome(Screen):
    pass
class FacDetF(Screen):
    pass
class StdDetF(Screen):
    pass

class StdHome(Screen):
    pass

	
sm = Builder.load_string("""
ScreenManager:
    ScreenZero:
        name:"screen0"
        id : id0
        Image:
            padding:20
            pos : root.pos
            source : "clg.png"
        BoxLayout:
            spacing:350
            padding:50
            orientation : "vertical"
            Label:
                text : "Welcome to Guru Nanak Institutions"
                color:(0, 0, 0, 1)
                font_size : 40
            Button:
                text : "START"
                font_size : 20
                on_release:
                    root.current = "who"

    Who:
        name : "who"
        id : whor
        BoxLayout:
            spacing : 25
            padding : 150
            orientation: "vertical"
            Label:
                text : "I am.."
                color : (0, 0, 0, 1)
                font_size : 40
            Button:
                text : "Management"
                font_size : 20
                on_release:
                    root.current = "loginOrRegMgmt"
            Button:
                text : "Faculty"
                font_size : 20
                on_release:
                    root.current = "loginOrRegFac"
            Button:
                text : "Student"
                font_size : 20
                on_release:
                    root.current = "loginOrRegStd"
    LoginOrRegMgmt:
        name : "loginOrRegMgmt"
        id : logM
        BoxLayout:
            spacing : 25
            padding : 100
            orientation : "vertical"
            Label:
                text : "Management Login"
                color : (0, 0, 0, 1)
                font_size : 40
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Username:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Password:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
                    password : True
            Button:
                text : "Login"
                on_release:
                    root.current = "mgmtHome"
                    

    LoginOrRegFac:
        name : "loginOrRegFac"
        id : logF
        BoxLayout:
            spacing : 25
            padding : 100
            orientation : "vertical"
            Label:
                text : "Faculty Login"
                color : (0, 0, 0, 1)
                font_size : 40
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Username:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Password:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
                    password : True
            Button:
                text : "Login"
                on_release:
                    root.current = "facHome"
            Label:
                text : "No account?"
                color:(0, 0, 0, 1)
            Button:
                text : "Register"
                on_release:
                    root.current="regFac"
                    
    RegFac:
        name : "regFac"
        id : regF
        BoxLayout:
            spacing : 25
            padding : 100
            orientation : "vertical"
            Label:
                text : "Faculty Registration"
                color : (0, 0, 0, 1)
                font_size : 40
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Full Name:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Email ID:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Password:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
                    password : True
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Retype Password:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
                    password : True
            Button:
                text : "Register"
                on_release:
                    root.current = "facHome"

    LoginOrRegStd:
        name : "loginOrRegStd"
        id : logS
        BoxLayout:
            spacing : 25
            padding : 100
            orientation : "vertical"
            Label:
                text : "Student Login"
                color : (0, 0, 0, 1)
                font_size : 40
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Username:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Password:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
                    password : True
            Button:
                text : "Login"
                on_release:
                    root.current = "stdHome"
            Label:
                text : "No account?"
                color:(0, 0, 0, 1)
            Button:
                text : "Register"
                on_release:
                    root.current="regStd"
                    
    RegStd:
        name : "regStd"
        id : regS
        BoxLayout:
            spacing : 25
            padding : 100
            orientation : "vertical"
            Label:
                text : "Student Registration"
                color : (0, 0, 0, 1)
                font_size : 40
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Full Name:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Email ID:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Password:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
                    password : True
            BoxLayout:
                orientation : "horizontal"
                Label:
                    text : "Retype Password:"
                    color:(0, 0, 0, 1)
                TextInput:
                    focus : True
                    multiline : False
                    password : True
            Button:
                text : "Register"
                on_release:
                    root.current = "stdHome"


    MgmtHome:
        name : "mgmtHome"
        id : homeM
        BoxLayout:
            spacing : 25
            padding : 100
            orientation : "vertical"
            Label:
                text : "WELCOME"
                color : (0, 0, 0, 1)
                font_size : 40
            Label:
                text : "Tap on what do you want to see:"
                color : (0, 0, 0, 1)

            Button:
                text : "Faculty Details"
                on_release:
                    root.current = "facDetM"
            Button:
                text : "Student Details"
                on_release:
                    root.current = "stdDetM"
            Button:
                text : "Online Shopping"
                on_release:
                    root.current = "ShoppingM"
            Button:
                text : "Online Library"
                on_release:
                    root.current = "libraryM"
            Button:
                text :"Logout"
                on_release:
                    root.current = "screen0"

    FacDetM:
        name : "facDetM"
        id : "facM"
        BoxLayout:
            orientation : "vertical"
            Button:
                color: 1,1,1,1
                font_size: 15
                size_hint: 0.2,0.1
                text: "Back"
                on_release:
                    root.current = "mgmtHome"
                pos_hint: {"left":1, "top":1}	
                    
            GridLayout:
                cols : 3
                spacing : 20
                padding : [20, 10]
                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\hod.jpg"
                    Label:
                        text: "Dr. Jarupula Rajeshwar\\nB.Tech(CSE), M.Tech(CSE), Ph.D(CSE)\\nProfessor & HOD, Department of CSE "
                        color : (0, 0, 0, 1)

                Image:
                    padding:20
                    pos : root.pos
                    source : "clg.png"

                Image:
                    padding:20
                    pos : root.pos
                    source : "clg.png"
                Image:
                    padding:20
                    pos : root.pos
                    source : "clg.png"
                Image:
                    padding:20
                    pos : root.pos
                    source : "clg.png"
                Image:
                    padding:20
                    pos : root.pos
                    source : "clg.png"
    StdDetM:
        name : "stdDetM"
        id : "stdM"
        BoxLayout:
            orientation : "vertical"
            Button:
                color: 1,1,1,1
                font_size: 15
                size_hint: 0.2,0.1
                text: "Back"
                on_release:
                    root.current = "mgmtHome"
                pos_hint: {"left":1, "top":1}	
                    
            GridLayout:
                cols : 3
                spacing : 20
                padding : [20, 10]
                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\me.jpg"
                    Label:
                        text: "K.Koushik\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\srav.jpg"
                    Label:
                        text: "K.Sraveen\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\sri.jpg"
                    Label:
                        text: "K.T.Srijith\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\jmks.jpg"
                    Label:
                        text: "J.Mohana Krishna\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\shah.jpg"
                    Label:
                        text: "Shailesh Kumar\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

    FacHome:
        name : "facHome"
        id : homeF
        BoxLayout:
            spacing : 25
            padding : 100
            orientation : "vertical"
            Label:
                text : "WELCOME"
                color : (0, 0, 0, 1)
                font_size : 40
            Label:
                text : "Tap on what do you want to see:"
                color : (0, 0, 0, 1)

            Button:
                text : "My Details"
                on_release:
                    root.current = "facDetF"
            Button:
                text : "Student Details"
                on_release:
                    root.current = "stdDetF"
            Button:
                text : "Online Shopping"
                on_release:
                    root.current = "ShoppingM"
            Button:
                text : "Online Library"
                on_release:
                    root.current = "libraryM"
            Button:
                text :"Logout"
                on_release:
                    root.current = "screen0"
    FacDetF:
        name : "facDetF"
        id : "facF"
        BoxLayout:
            orientation : "vertical"
            Button:
                color: 1,1,1,1
                font_size: 15
                size_hint: 0.2,0.1
                text: "Back"
                on_release:
                    root.current = "facHome"
                pos_hint: {"left":1, "top":1}
            BoxLayout:
                orientation : "vertical"
                Image:
                    padding:20
                    pos : root.pos
                    source : "images\hod.jpg"
                Label:
                    text: "Dr. Jarupula Rajeshwar\\nB.Tech(CSE), M.Tech(CSE), Ph.D(CSE)\\nProfessor & HOD, Department of CSE "
                    color : (0, 0, 0, 1)

    StdDetF:
        name : "stdDetF"
        id : "stdF"
        BoxLayout:
            orientation : "vertical"
            Button:
                color: 1,1,1,1
                font_size: 15
                size_hint: 0.2,0.1
                text: "Back"
                on_release:
                    root.current = "facHome"
                pos_hint: {"left":1, "top":1}	
                    
            GridLayout:
                cols : 3
                spacing : 20
                padding : [20, 10]
                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\me.jpg"
                    Label:
                        text: "K.Koushik\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\srav.jpg"
                    Label:
                        text: "K.Sraveen\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\sri.jpg"
                    Label:
                        text: "K.T.Srijith\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\jmks.jpg"
                    Label:
                        text: "J.Mohana Krishna\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

                BoxLayout:
                    orientation : "vertical"
                    Image:
                        padding:20
                        pos : root.pos
                        source : "images\student\shah.jpg"
                    Label:
                        text: "Shailesh Kumar\\nYear  :  III\\nDepartment : CSE\\nSection  : II"
                        color : (0, 0, 0, 1)

        

        
""")

class TestApp(App):
	def build(self):
		Window.clearcolor=(1, 1, 1, 0.8)
		return sm
	
if __name__=='__main__':
	TestApp().run()
