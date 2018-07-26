from kivy.properties import NumericProperty
from kivy.animation import Animation
from kivy.uix.label import Label
import math

class CountdownTimer(Label):
    a = NumericProperty(3600)

    def start(self):
        Animation.cancel_all(self)
        self.anim = Animation(a=0, duration=self.a)

        def finish_callback(animation, incr_crude_clock):
            incr_crude_clock.text = "00."

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def stop(self):
        self.anim.stop(self)

    def on_a(self, instance, value):
        self.text = str(math.floor(value/60)) + ':' + str(round(value%60, 1))