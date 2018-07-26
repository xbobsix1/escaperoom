from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from escaperoom.widgets import CountdownTimer



class EscapeRoom(BoxLayout):
    def __init__(self, **kwargs):
        super(EscapeRoom, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.layout2 = PasswordLayout()
        self.add_widget(self.layout2)

        self.countdown = CountdownTimer(font_size=50,
                                        bold=True)
        self.countdown.start()
        self.add_widget(self.countdown)
        
        self.img = Image(source='WHO.jpg',
                         allow_stretch=True)

        self.passwordBox = FloatLayout()

        self.add_widget(self.img)
        self.add_widget(self.passwordBox)

        self.textinput = TextInput(hint_text='Password',
                                   multiline=False,
                                   size_hint=(.7, .1),
                                   pos_hint={'x': .15, 'y': .5})

        self.passwordBox.add_widget(self.textinput)

        self.btn = Button(text='CHECK',
                          size_hint=(.4, .1),
                          pos_hint={'x': .3, 'y': .3})

        self.passwordBox.add_widget(self.btn)

from escaperoom.main import next_stage
class PasswordLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(PasswordLayout, self).__init__(**kwargs)



class RapportLayout(BoxLayout):
    def __init__(self, **kwargs):
        self.orientation = 'vertical'
        self.img = Image(source='WHO.jpg',
                         allow_stretch=True)

        self.passwordBox = FloatLayout()

        self.add_widget(self.img)
        self.add_widget(self.passwordBox)

        self.textinput = TextInput(hint_text='wqdwqdqwd',
                                   multiline=False,
                                   size_hint=(.7, .1),
                                   pos_hint={'x': .15, 'y': .5})

        self.passwordBox.add_widget(self.textinput)

        self.btn = Button(text='CHascascascECK',
                          size_hint=(.4, .1),
                          pos_hint={'x': .3, 'y': .3})

        self.passwordBox.add_widget(self.btn)