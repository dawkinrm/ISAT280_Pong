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
import pong

class TitleLabel(Label):
  pass

class MainMenuScreen(Screen):
  pass

class AboutScreen(Screen):
  pass
  
class HelpScreen(Screen):
  pass

class PongScreen(Screen):
    Window.clearcolor = (1, 1, 1, 1)
  
class ConfigScreen(Screen):
  pass  

class BackButton(Button):
  pass	
  
class MyScreenManager(ScreenManager):
  pass

class Cmenu(Bubble):

    def menu_selected(self, *l):
        if l[0].text == 'hows':
            # move to sub menu
            Animation(scroll_x = 1, d=.5 ).start(l[0].parent.parent.parent)
            #l[0].parent.parent.parent change this and everything relative to something non-relative if you want-to make the menu more extensible
        elif l[0].text == '<':
            # move back to root menu
            Animation(scroll_x = 0, d=.5 ).start(l[0].parent.parent.parent)
        else:
            #fade out animation
            (r, g, b, a) = self.parent.context_menu.background_color

            def on_anim_complete(*l):
                self.parent.context_menu.background_color = (r, g, b, a)
                self.parent.remove_widget(self.parent.context_menu)

            anim = Animation(background_color = (0, 0, 0, 0), d=.1 )
            anim.start(self.parent.context_menu)
            anim.bind(on_complete = on_anim_complete)
            print l[0].text + ' selected'

class PongGUIApp(App):
  Window.size = (325, 455)
  Window.clearcolor = (255, 255, 255, 1)
  pong_game = pong.PongApp()


#launcher = InteractiveLauncher(PongGUIApp())
#launcher.run()
if __name__ == "__main__":
  PongGUIApp().run()
