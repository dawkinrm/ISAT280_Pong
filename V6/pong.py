from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.interactive import InteractiveLauncher
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label

class PongPaddle(Widget):
    """ Represents a 'Pong' paddle """
    score = NumericProperty(0)

    def bounce_ball(self, ball):
    #Simulates bouncing of a ball off the pong paddle
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    """ Represents a 'Pong' ball """
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
    #Give the new position of the pong ball
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    """ Represents a 'Pong' game """
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    score_limit = NumericProperty(10)
        
    def serve_ball(self, vel=(4, 0)):
        #Creates a new pong ball and sets the defualt velocity
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        #Creates the visual update of the pong gam
        self.ball.move()

        #bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        #bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        #went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        #Creates movement for on_touch of player pong paddles
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

class MenuWidget(Widget):
    """ Represents a pause and resume menu """
    visible = False

class PongApp(App):
    def build(self):
        #Window.clearcolor = (.50, .50, .50, 1)
        self.menu = MenuWidget()
        self.game = PongGame()
        self.game.serve_ball()
        Clock.schedule_interval(self.game.update, 1.0 / 60.0)
        Clock.schedule_interval(self.check_game_over, 1.0 / 60.0)
        return self.game
            
    def check_game_over(self, dt):
        #checks whether the game is over or not
        if self.game.player1.score >= self.game.score_limit:
            self.pause()
            self.show_winner(self.game.player1.name)
                  
        if self.game.player2.score >= self.game.score_limit:
            self.pause()
            self.show_winner(self.game.player2.name)
    
    def show_winner(self, winner_name):
        #adds the winners name to the winner banner and displays the banner
        l = Label(text=winner_name + " WINS!")
        l.color = 0,0,0,1
        l.bold = True
        l.size = self.root.size
        l.font_size = 80
        self.root.add_widget(l)
        
    
    def stop(self):
        #Completely stops the pong game app
        self.stop()
    
    def pause(self):
        #Pauses the pong game
        Clock.unschedule(self.game.update)

    def resume(self):
        #Resumes the pong game
        Clock.schedule_interval(self.game.update, 1.0 / 60.0)

    def show_menu(self):
        #Shows the menu widget
        if not self.menu.visible:
            self.pause()
            self.menu.visible = True
            self.root.add_widget(self.menu)

    def close_menu(self):
        #Removes visibility of the menu
        if self.menu.visible:
            self.menu.visible = False
            self.root.remove_widget(self.menu)
            self.resume()
    
#i = InteractiveLauncher(PongApp())


#if __name__ == '__main__':
#   PongApp().run()

