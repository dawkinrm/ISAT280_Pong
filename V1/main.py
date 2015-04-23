# Mini-Project_1 Deliverable
# Justin Conners, Reyna Dawkins
# ISAT 280
# February 24, 2015

from kivy.app import App
from kivy.core.window import Window

class PongApp(App):
  Window.size = (325, 455)
  Window.clearcolor = (255, 255, 255, 1)

if __name__ == "__main__":
  PongApp().run()
