# Mini-Project_2 Deliverable
# Justin Conners, Reyna Dawkins
# ISAT 280
# March 26, 2015

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.interactive import InteractiveLauncher
from kivy.graphics.fbo import Fbo
from kivy.graphics import ClearColor, ClearBuffers, Canvas, Rectangle, Color
import pong
import dbconnect

player1 = ObjectProperty(None)
player2 = ObjectProperty(None)

class TitleLabel(Label):
    pass

class MainMenuScreen(Screen):
    pass

class AboutScreen(Screen):
    pass
  
class HelpScreen(Screen):
    pass

class LeaderboardScreen(Screen):
    def returnMatches(self):
        db = dbconnect.connect()
        self.ids["test"].text = str(db[6]) + " " + str(db[2]) + " " + str(db[4]) + "\n" + str(db[1]) + " " + str(db[3])

class PongScreen(Screen):
    Window.clearcolor = (0, 0, 0, 1)
  
class ConfigScreen(Screen):
    def setNames(self, p1, p2):
        self.player1.name = p1[:10]
        self.player2.name = p2[:10]
    
    def getP1Name(self):
        return self.player1.name
       
    def getP2Name(self):
        return self.player2.name

class BackButton(Button):
    pass	

class MyScreenManager(ScreenManager):
    pass

class PongGUIApp(App):
    title = 'PongApp'
    #Window.size = (325, 455)
    Window.clearcolor = (0, 1, 1, 1) 
    pong_game = pong.PongApp()


#launcher = InteractiveLauncher(PongGUIApp())
#launcher.run()

if __name__ == "__main__":
    PongGUIApp().run()