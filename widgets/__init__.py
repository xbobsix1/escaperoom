from kivy.properties import StringProperty, NumericProperty
from kivy.animation import Animation
from kivy.animation import AnimationTransition
from kivy.uix.progressbar import ProgressBar
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
                self.text = '00:00:00'
                self.fail_callback()

        self.anim.bind(on_complete=finish_callback)
        self.anim.start(self)

    def stop(self):
        self.anim.stop(self)

    def on_a(self, instance, value):
        minutes = str(math.floor(value / 60))
        seconds = str(round(value % 60, 2))

        if len(minutes) == 1:
            minutes = '0' + minutes

        if seconds[1] == '.':
            seconds = '0' + seconds
        if len(seconds) < 5:
            seconds += '0'

        self.text = minutes + ':' + seconds


class CustomProgressBar(ProgressBar):
    a = NumericProperty(0)
    t = NumericProperty(2)

    def __init__(self, callback, **kwargs):
        super(CustomProgressBar, self).__init__(**kwargs)
        self.progress = Animation(value=20 + 20 * self.a, t='out_circ', duration=self.t)

        self.progress.start(self)
        self.callback = callback

        def finish_callback(animation, progress):
            self.callback()

        self.progress.bind(on_complete=finish_callback)
