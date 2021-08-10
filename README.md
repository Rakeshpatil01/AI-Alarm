# AI-Alarm
Alarm for students and professional. 
kivy :
     FloatButton:
        id:cta
        pos_hint: {"center_x":0.5, "center_y":0.5}

python:
     def breath(self, *args):
        anim = Animation(btn_size=(20, 20), t='in_quad', duration=.5) + \
            Animation(btn_size=(70, 70), t='in_quad', duration=.5)
        tgt = self.ids.cta
        anim.start(tgt)

    Clock.schedule_interval(clock.breath, 1)