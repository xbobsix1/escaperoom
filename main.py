from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.video import Video
from escaperoom.widgets import CountdownTimer
from escaperoom.widgets import KeyboardListener
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import escaperoom.custom_lib
from kivy.core.window import Window


class IntroLogo(Screen):
    def __init__(self, **kwargs):
        super(IntroLogo, self).__init__(**kwargs)

        # Add starting Logo
        self.logo = Image(source='WHO.jpg')
        self.add_widget(self.logo)

        ## Specific function that unbinds a KeyboardsListener and then switches to next screen
        def switch():
            self.keyboardListener.unbind()
            self.remove_widget(self.keyboardListener)
            sm.switch_to(VideoScreen())

        # Add custom KeyBoardListener that triggers the switch-function on enter-key
        self.keyboardListener = KeyboardListener('enter', switch)
        self.add_widget(self.keyboardListener)


class VideoScreen(Screen):
    def __init__(self, **kwargs):
        super(VideoScreen, self).__init__(**kwargs)
        self.video = Video(source='test.mkv', state='stop')

        # Specific function that switches to EscapeRoom screen
        def switch(self, kwargs):
            sm.switch_to(PasswordScreen())

        # Bind a callback to eos event. Eos is when the video ends
        self.video.bind(eos=switch)
        self.add_widget(self.video)

    # When the screen enters view, play the video
    def on_enter(self, *args):
        self.video.state = 'play'


class PasswordScreen(Screen):
    def __init__(self, **kwargs):
        super(PasswordScreen, self).__init__(**kwargs)
        this = self
        self.layout = BoxLayout(orientation='horizontal')
        self.add_widget(self.layout)
        self.layout2 = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.layout2)

        # Start the global timer and add a Label to EscapeRoom > layout
        timer.start()
        self.countdown = Label(text=timer.text, font_size=50, bold=True)
        self.layout.add_widget(self.countdown)

        # Set the countdown-label to be equal to our global timer
        def update(dt):
            self.countdown.text = timer.text

        # Update our ocuntdown-text every
        Clock.schedule_interval(update, 1.0 / 15.0)

        self.img = Image(source='WHO.jpg',
                         allow_stretch=True)

        self.passwordBox = FloatLayout()

        self.layout2.add_widget(self.img)
        self.layout2.add_widget(self.passwordBox)

        self.textinput = TextInput(hint_text='Password',
                                   multiline=False,
                                   size_hint=(.7, .1),
                                   pos_hint={'x': .15, 'y': .5})

        def check_password(self):
            if sm.get_screen(sm.current).textinput.text == '123':
                switch()

        self.btn = Button(text='CHECK',
                          size_hint=(.4, .1),
                          pos_hint={'x': .3, 'y': .3},
                          on_press=check_password)

        self.passwordBox.add_widget(self.textinput)
        self.passwordBox.add_widget(self.btn)

        def switch():
            sm.switch_to(RapportScreen())


class RapportScreen(Screen):
    def __init__(self, **kwargs):
        super(RapportScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='horizontal')
        self.add_widget(self.layout)
        self.layout2 = BoxLayout(orientation='vertical', padding=[20,20])
        self.layout.add_widget(self.layout2)

        # Start the global timer and add a Label to EscapeRoom > layout
        timer.start()
        self.countdown = Label(text=timer.text, font_size=50, bold=True)
        self.layout.add_widget(self.countdown)

        # Set the countdown-label to be equal to our global timer
        def update(dt):
            self.countdown.text = timer.text

        # Update our ocuntdown-text every
        Clock.schedule_interval(update, 1.0 / 15.0)

        # Adding the layout of the entire left side
        self.agent = Label(text='DISEAS AGENT', font_size=20)
        self.agent_input = TextInput(multiline=False)

        self.zero_name = Label(text='PATIENT ZERO NAME', font_size=20)
        self.zero_name_input = TextInput(multiline=False)

        self.structure = Label(text='MOLECULE STRUCTURE', font_size=20)

        self.double_bond = Label(text='DOUBLE BONDS', font_size=20)
        self.double_bond_input = TextInput(multiline=False)

        self.triple_bond = Label(text='TRIPLE BONDS', font_size=20)
        self.triple_bond_input = TextInput(multiline=False)

        self.check_button = Button(text='GENERATE', font_size=40)

        self.layout2.add_widget(self.agent)
        self.layout2.add_widget(self.agent_input)
        self.layout2.add_widget(self.zero_name)
        self.layout2.add_widget(self.zero_name_input)
        self.layout2.add_widget(self.structure)
        self.layout2.add_widget(self.double_bond)
        self.layout2.add_widget(self.double_bond_input)
        self.layout2.add_widget(self.triple_bond)
        self.layout2.add_widget(self.triple_bond_input)
        self.layout2.add_widget(self.check_button)

        def switch():
            # sm.switch_to(xxxxx)
            pass

        def check_info():

            correct_answers = 0

            if self.agent_input.text.lower() == '123':
                correct_answers += 1

            if self.zero_name_input.text == '123':
                correct_answers += 1

            if '123' in self.double_bond_input.text:
                correct_answers += 1

            if self.triple_bond_input.text == '123':
                correct_answers += 1

            # (WIP) REPLACE THE LEFT LAYOUT FOR 10 SECONDS WHILE ANIMATING A PROGRESS BAR. IF AFTER THE FACT THERE
                # ARE 4 CORRECT ANSWERS, THEN PROCCED TO VICTORY SCREEN. IF THERE IS AN INCORRECT ANSWER,
                # MARK THE INCORRECT INFORMATION AS RED AND BOLD. REMOVE ON FOCUS

# Window.fullscreen = True

# Add a global timer, that keeps track of the countdown between Screens
global timer
timer = CountdownTimer()

# Add a screen manager and a starting screen
sm = ScreenManager()
sm.add_widget(IntroLogo())


class Main(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Main().run()
