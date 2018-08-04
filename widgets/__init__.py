from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.uix.widget import Widget
import math
import keyboard


class CountdownTimer(Widget):
    a = NumericProperty(5)
    text = StringProperty('60:00.00')

    def __init__(self, fail_callback, **kwargs):
        super().__init__(**kwargs)
        self.fail_callback = fail_callback

    def start(self):
        Animation.cancel_all(self)
        self.anim = Animation(a=0, duration=self.a)

        def finish_callback(animation, incr_crude_clock):
            if self.a > 0:
                incr_crude_clock.text = self.text
            else:
                self.text = '00:00'
                self.fail_callback()

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

        this = self
        def add_time(delta_time):
            print(self.a)
            self.anim.stop(self)
            self.a = self.a + delta_time
            self.anim.start(self)
            print(self.a)

        # Add hotkeys
        keyboard.add_hotkey('ctrl+g+1', add_time, args=[-300])
        keyboard.add_hotkey('ctrl+g+2', add_time, args=[300])
        keyboard.add_hotkey('ctrl+p+1', self.anim.stop, args=[self])
        keyboard.add_hotkey('ctrl+p+2', self.anim.start, args=[self])

    def stop(self):
        keyboard.remove_all_hotkeys()
        self.anim.stop(self)

    def on_a(self, instance, value):
        minutes = str(math.floor(value / 60))
        seconds = str(math.floor(value % 60))

        if len(minutes) == 1:
            minutes = '0' + minutes

        if len(seconds) == 1:
            seconds = '0' + seconds

        self.text = minutes + ':' + seconds


class CustomProgressBar(ProgressBar):
    a = NumericProperty(0)
    t = NumericProperty(10)

    def __init__(self, callback, **kwargs):
        super(CustomProgressBar, self).__init__(**kwargs)
        self.progress = Animation(value=20 + 20 * self.a, t='out_circ', duration=self.t)

        self.progress.start(self)
        self.callback = callback

        def finish_callback(animation, progress):
            self.callback()

        self.progress.bind(on_complete=finish_callback)
