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
from plyer import accelerometer, vibrator
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
import dbconnect
import random
import pong


class TitleLabel(Label):
    pass


class MainMenuScreen(Screen):
    ball = ObjectProperty(None)
    
    def start(self):
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        
    def try_with_accel(self):
        vals = accelerometer.acceleration[:3]
        print "THE VALUES ARE HERE: ", vals
        if ((vals[0] and vals[1]) != None) and (vals[0] + vals[1]) > 10:
            Clock.schedule_interval(self.update, 1.0 / 60.0)
            self.serve_ball()
    
    def serve_ball(self, vel=(10, random.randint(-10,10))):
        #Creates a new pong ball and sets the defualt velocity
        #self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        #Creates the visual update of the pong gam
        self.ball.move()

        #bounce ball off wall
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1
        if (self.ball.x < self.x) or ((self.ball.x + self.ball.size[0]) > self.width):
            self.ball.velocity_x *= -1
        
#`Clock.schedule_interval(try_with_accel, 1.0 / 60.0)

class AboutScreen(Screen):
    pass
  
  
class HelpScreen(Screen):
    pass

class Leaderboard(BoxLayout):
	def __init__(self, **kwargs):
			super(Leaderboard, self).__init__(**kwargs)
			self.orientation = 'vertical'
			self.rows = dbconnect.pull()
			self.box = BoxLayout()
			self.col1 = Label(text="[b]Player 1[/b]", markup=True)
			self.col2 = Label(text="[b]Score[/b]", markup=True)
			self.col3 = Label(text="[b]Player 2[/b]", markup=True)
			self.col4 = Label(text="[b]Score[/b]", markup=True)
			self.col5 = Label(text="[b]Date[/b]", markup=True)
			self.box.add_widget(self.col1)
			self.box.add_widget(self.col2)
			self.box.add_widget(self.col3)
			self.box.add_widget(self.col4)
			self.box.add_widget(self.col5)
			self.add_widget(self.box)
			self.add_widget(Label(text="---------------------------------------------------------------------------------------------"))
			
			for row in self.rows:
				self.bx = BoxLayout()
				self.p1 = Label(text=str(row[0]))
				self.p1s = Label(text=str(row[2]))
				self.p2 = Label(text=str(row[1]))
				self.p2s = Label(text=str(row[3]))
				self.dateL = Label(text=str(row[5]))
				self.bx.add_widget(self.p1)
				self.bx.add_widget(self.p1s)
				self.bx.add_widget(self.p2)
				self.bx.add_widget(self.p2s)
				self.bx.add_widget(self.dateL)
				self.add_widget(self.bx)

class LeaderboardScreen(Screen):
		def build(self):
				return Leaderboard()
			

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
    
    try:
        accelerometer.enable()
    except Exception, e:
        print str(e)
        
    pong_game = pong.PongApp()


#i = InteractiveLauncher(PongGUIApp())
#i.run()

if __name__ == "__main__":
    PongGUIApp().run()
