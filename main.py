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


class EscapeRoom(App):
    def build(self):
        #Window.fullscreen = True
        layout = BoxLayout(orientation='horizontal')
        layout2 = BoxLayout(orientation='vertical')
        layout.add_widget(layout2)

        countdown = CountdownTimer(font_size=50,
                                   bold=True)
        countdown.start()

        img = Image(source='WHO.jpg',
                    allow_stretch=True)

        passwordBox = FloatLayout()

        layout.add_widget(countdown)
        layout2.add_widget(img)
        layout2.add_widget(passwordBox)

        textinput = TextInput(hint_text='Password',
                              multiline=False,
                              size_hint=(.7, .1),
                              pos_hint={'x': .15, 'y': .5})

        def CheckPassword(self):
            if textinput.text == '123':
                btn.text = 'lala'


        btn = Button(text='CHECK',
                     size_hint=(.4, .1),
                     pos_hint={'x': .3, 'y': .3},
                     on_press=CheckPassword)

        passwordBox.add_widget(textinput)
        passwordBox.add_widget(btn)

        return layout

if __name__ == "__main__":
    EscapeRoom().run()
