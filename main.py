from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from escaperoom.widgets import CountdownTimer
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class EscapeRoom(BoxLayout):
    def __init__(self, **kwargs):
        super(EscapeRoom, self).__init__(**kwargs)
        # Window.fullscreen = True
        self.orientation = 'horizontal'
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
