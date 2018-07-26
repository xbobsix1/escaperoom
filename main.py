import math
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window

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


class EscapeRoom(BoxLayout):

    def __init__(self, **kwargs):
        super(EscapeRoom, self).__init__(**kwargs)
        #Window.fullscreen = True
        self.orientation='horizontal'
        self.layout2 = BoxLayout(orientation='vertical')
        self.add_widget(self.layout2)

        self.countdown = CountdownTimer(font_size=50,
                                   bold=True)
        self.countdown.start()

        self.img = Image(source='WHO.jpg',
                    allow_stretch=True)

        self.passwordBox = FloatLayout()

        self.add_widget(self.countdown)
        self.layout2.add_widget(self.img)
        self.layout2.add_widget(self.passwordBox)

        self.textinput = TextInput(hint_text='Password',
                              multiline=False,
                              size_hint=(.7, .1),
                              pos_hint={'x': .15, 'y': .5})

        self.btn = Button(text='CHECK',
                     size_hint=(.4, .1),
                     pos_hint={'x': .3, 'y': .3})

        self.passwordBox.add_widget(self.textinput)
        self.passwordBox.add_widget(self.btn)


class Main(App):

    global stage
    stage = 2

    def build(self):
        def switch(stage):
            switcher = {
                0: "zero",
                1: "one",
                2: EscapeRoom(),
            }
            return switcher.get(stage, "0")
        return switch(stage)

if __name__ == "__main__":
    Main().run()
