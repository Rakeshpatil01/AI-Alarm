from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivymd.uix.floatlayout import MDFloatLayout
from math import cos, sin, pi
from kivy.clock import Clock
from kivy.properties import NumericProperty
import datetime
from kivy.lang import Builder
from kivy.properties import ObjectProperty


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
            Line(points=[self.center_x, self.center_y, self.center_x+0.8*self.r*sin(pi/30 *
                 time.second), self.center_y+0.8*self.r*cos(pi/30*time.second)], width=1, cap="round")
            Color(0.3, 0.6, 0.3)
            Line(points=[self.center_x, self.center_y, self.center_x+0.7*self.r*sin(pi/30 *
                 time.minute), self.center_y+0.7*self.r*cos(pi/30*time.minute)], width=2, cap="round")
            Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x, self.center_y, self.center_x+0.5*self.r*sin(
                pi/360*th), self.center_y+0.5*self.r*cos(pi/360*th)], width=3, cap="round")


class ClockWidget(MDScreen):

    def on_enter(self):
        Clock.schedule_interval(self.ticks.update_clock, 1)


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class AIAlarm(MDApp):
    def build(self):
        # theme style
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        # self.theme_cls.primary_hue = "500"

        return Builder.load_file('design.kv')


if __name__ == '__main__':
    AIAlarm().run()
