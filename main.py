from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.label import MDLabel
from kivy.uix.widget import Widget
from kivy.clock import Clock
import datetime
from kivy.graphics import Color, Line
from math import cos, sin, pi


class ContentNavigationDrawer(MDBoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''


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
            Line(points=[self.center_x,
                         self.center_y,
                         self.center_x+0.8*self.r*sin(pi/30 * time.second),
                         self.center_y+0.8*self.r*cos(pi/30*time.second)],
                 width=1,
                 cap="round")

            Color(0.3, 0.6, 0.3)
            Line(points=[self.center_x,
                         self.center_y,
                         self.center_x+0.7*self.r*sin(pi/30 * time.minute),
                         self.center_y+0.7*self.r*cos(pi/30*time.minute)],
                 width=2,
                 cap="round")

            Color(0.4, 0.7, 0.4)
            th = time.hour*60 + time.minute
            Line(points=[self.center_x,
                         self.center_y,
                         self.center_x+0.5*self.r*sin(pi/360*th),
                         self.center_y+0.5*self.r*cos(pi/360*th)],
                 width=3,
                 cap="round")


class Example(MDApp):
    def build(self):
        return Builder.load_file('design.kv')

    def on_start(self):
        for x in range(1, 13):
            self.root.ids.ClockAlalrm.add_widget(
                MDLabel(text=f'{x}', color=[0, 0, 0, 1])
            )
        Clock.schedule_interval(self.root.ids.ticks.update_clock, 1)


Example().run()
