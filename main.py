from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


class EscapeRoom(App):
    def build(self):
        #Window.fullscreen = True
        layout = BoxLayout(orientation='horizontal')
        layout2 = BoxLayout(orientation='vertical')
        layout.add_widget(layout2)

        countdown = Label(text='00:00', bold=True, font_size=50)
        img = Image(source='WHO.jpg', allow_stretch=True)
        layout.add_widget(countdown)
        layout2.add_widget(img)
        passwordBox = FloatLayout()
        layout2.add_widget(passwordBox)
        textinput = TextInput(hint_text='Password', multiline=False, size_hint=(.7, .1), pos_hint={'x': .15, 'y': .5})
        btn = Button(text='CHECK', size_hint=(.4, .1), pos_hint={'x': .3, 'y': .3})
        passwordBox.add_widget(textinput)
        passwordBox.add_widget(btn)

        return layout


if __name__ == "__main__":
    EscapeRoom().run()
