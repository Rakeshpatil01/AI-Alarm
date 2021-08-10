import datetime
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
# from kivy.uix.floatlayout import FloatLayout
from math import cos, sin, pi
from kivy.clock import Clock
from kivy.lang import Builder
# from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (480, 800)
# from kivy.properties import NumericProperty


class MyClockWidget(Screen):
    pass


class Ticks(Widget):
    def __init__(self, **kwargs):
        super(Ticks, self).__init__(**kwargs)
        self.bind(pos=self.update_clock)
        self.bind(size=self.update_clock)

    def update_clock(self, *args):
        self.canvas.clear()
        with self.canvas:
            time = datetime.datetime.now()
            Color(0.2, 0.5, 0.2)
            Line(
                points=[self.center_x,
                        self.center_y,
                        self.center_x + 0.8*self.r *
                        sin(pi/30 * time.second),
                        self.center_y+0.8*self.r*cos(pi/30*time.second)],
                width=1,
                cap="round")
            Color(0.3, 0.6, 0.3)
            Line(
                points=[self.center_x,
                        self.center_y,
                        self.center_x+0.7*self.r*sin(pi/30 * time.minute),
                        self.center_y+0.7*self.r*cos(pi/30*time.minute)],
                width=2,
                cap="round")
            Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            Line(
                points=[self.center_x,
                        self.center_y,
                        self.center_x+0.5*self.r*sin(pi/360*th),
                        self.center_y+0.5*self.r*cos(pi/360*th)],
                width=3,
                cap="round")


Builder.load_file('design.kv')


class MyClockApp(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MyClockWidget(name="screen_one"))
        clock = MyClockWidget()
        Clock.schedule_interval(clock.ticks.update_clock, 1)
        return clock


if __name__ == '__main__':
    MyClockApp().run()
