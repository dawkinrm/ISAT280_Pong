# Mini-Project_1 Deliverable
# Justin Conners, Reyna Dawkins
# ISAT 280
# February 24, 2015

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
import pongGame as pg


class TitleLabel(Label):
  pass

class MenuScreen(Screen):
  pass

class AboutScreen(Screen):
  pass
  
class HelpScreen(Screen):
  pass

class PongScreen(Screen):
  """
  def build(self):
    game = PongGame()
    game.serve_ball()
    Clock.schedule_interval(game.update, 1.0 / 60.0)
    return game
  """
  pass

class ConfigScreen(Screen):
  pass  

class BackButton(Button):
  pass	
  
class MyScreenManager(ScreenManager):
  pass  

class PongApp(App):
  Window.size = (325, 455)
  Window.clearcolor = (255, 255, 255, 1)
  

if __name__ == "__main__":
  PongApp().run()
