from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.video import Video
from kivy.core.window import Window
from kivy.uix.widget import Widget
import math


class KeyboardListener(Widget):
    def __init__(self, key, callback, **args):
        super(KeyboardListener, self).__init__()
        self.key = key
        self.callback = callback
        self.args = args
        self.activated = True
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if self.activated and keycode[1] == 'enter':
            return self.callback(**self.args)

        return True

    def unbind(self, **kwargs):
        self.activated = False


class CountdownTimer(Widget):
    a = NumericProperty(3600)
    text = StringProperty('0')
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
        seconds = str(round(value % 60, 2))
        if len(seconds) < 5:
            seconds += '0'
        self.text = str(math.floor(value / 60)) + ':' + seconds
