# Justin Conners, Reyna Dawkins
# ISAT 280
# Spring 2015

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
from kivy.uix.dropdown import DropDown
import pong


class TitleLabel(Label):
    pass

class MainMenuScreen(Screen):
    pass

class AboutScreen(Screen):
    pass
  
class HelpScreen(Screen):
    pass

class LeaderboardScreen(Screen):
    pass

class PongScreen(Screen):
    Window.clearcolor = (0, 0, 0, 1)
    
    def getLimit(self):
    # Im not sure why this screen needs this. But it does.
        return 1
  
class ConfigScreen(Screen):
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    scoreLimit = NumericProperty(None)
    defaultLimit = NumericProperty(10)
    
    def setNames(self, p1, p2):
    # Sets Player names. If no name is set,
    # Use default player names
        if p1 == "":
            self.player1.name = "Player 1"
        else:
            self.player1.name = p1[:10]
        if p2 == "":  
            self.player2.name = "Player 2"
        else:
            self.player2.name = p2[:10]
    
    def getP1Name(self):
    # Returns player1 name
        return self.player1.name
       
    def getP2Name(self):
    # Returns player2 name
        return self.player2.name
		
    def setLimit(self, num):
    # Sets the games score limit
        if num != None:
            self.scoreLimit = int(num)
        else:
            self.scoreLimit = self.defaultLimit
		
    def getLimit(self):
    # Returns the game's score limit
        if self.scoreLimit != None:
            return self.scoreLimit
        else:
            return self.defaultLimit

class BackButton(Button):
    pass	
		
class MyScreenManager(ScreenManager):
    pass

class PongGUIApp(App):
    title = 'PongApp'
    #Window.size = (325, 455)
    Window.clearcolor = (.55, .55, .84, 1) 
    pong_game = pong.PongApp()
    
    def vib(self):
        vibrator.vibrate(1000)

#launcher = InteractiveLauncher(PongGUIApp())
#launcher.run()

if __name__ == "__main__":
    PongGUIApp().run()
