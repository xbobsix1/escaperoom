import os

os.environ["KIVY_IMAGE"] = "pil"

from kivy.config import Config

Config.set('kivy', 'exit_on_escape', '0')
Config.set('kivy', 'keyboard_mode', 'system')
Config.set('graphics', 'fullscreen', '1')
Config.set('graphics', 'allow_screensaver', '0')
Config.set('graphics', 'width', '1920')
Config.set('graphics', 'height', '1080')

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.loader import Loader
from kivy import resources
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import focus
from kivy.uix.video import Video
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.clock import Clock
from kivy.properties import NumericProperty
from widgets import *
import re
import keyboard
from kivy.core.window import Window
from kivy.cache import Cache
Cache._categories['kv.image']['limit'] = 0
Cache._categories['kv.texture']['limit'] = 0

# from gpiozero import LED


# Retrieve data files
Builder.load_file('./layout.kv')
gif = Loader.image('./timer_frame.gif')
logo = Loader.image('./WHO.png')
check = Loader.image('./Check.png')
check_hover = Loader.image('./Check Hover.png')


class IntroLogo(BgScreen):
    def __init__(self, **kwargs):
        super(IntroLogo, self).__init__(**kwargs)

        self.layout = AnchorLayout(padding=[100])
        self.add_widget(self.layout)

        # Add starting Logo
        self.logo = Image(source='WHO.png',
                          allow_stretch=True,
                          keep_ratio=True)
        self.layout.add_widget(self.logo)

        # Specific function that removes a KeyboardsListener and then switches to next screen
        def switch():
            keyboard.remove_hotkey(self.hotkey)
            sm.switch_to(VideoScreen())

        # Add custom KeyBoardListener that triggers the switch-function on enter-key
        self.hotkey = keyboard.add_hotkey('enter', switch)


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


class PasswordScreen(BgScreen):
    def __init__(self, **kwargs):
        super(PasswordScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='horizontal')
        self.add_widget(self.layout)
        self.layout2 = BoxLayout(orientation='vertical', padding=[0, 50])
        self.layout.add_widget(self.layout2)
        self.layout_count = AnchorLayout(size_hint=(.9, 1))
        self.layout.add_widget(self.layout_count)

        # Start the global timer and add a Label to EscapeRoom > layout
        timer.start()
        self.timer_frame = Image(source='timer_frame.gif',
                                 anim_delay=0.05,
                                 width=600,
                                 allow_stretch=True,
                                 keep_ratio=True)
        self.layout_count.add_widget(self.timer_frame)
        self.countdown = CountdownText(text=timer.text)
        self.layout_count.add_widget(self.countdown)

        # Set the countdown-label to be equal to our global timer
        def update(dt):
            self.countdown.text = timer.text

        # Update our ocuntdown-text every 1/15 seconds
        Clock.schedule_interval(update, 1.0 / 15.0)

        self.img = Image(source='WHO.png',
                         allow_stretch=True)

        self.passwordBox = FloatLayout()

        self.layout2.add_widget(self.img)
        self.layout2.add_widget(self.passwordBox)

        self.textinput = CustomTextInput(hint_text='Password',
                                         multiline=False,
                                         size_hint=(.6, .17),
                                         pos_hint={'center_x': .5, 'y': .55})

        self.passwordBox_wrong = Label(text='Incorrect password', color=(1, 0, 0, 0), font_size=20, bold=True,
                                       pos_hint={'center_x': .5, 'y': 0}, valign='top')

        # Switch screen if password is correct. Else, show error-label
        def check_password(PasswordScreen):
            if self.textinput.text == '123':
                switch()
            else:
                self.passwordBox_wrong.color = (1, 0, 0, 1)

        # Check button and passwordbox
        self.btn = ImageButton(on_press=check_password,
                               size_hint=(.3, None),
                               keep_ratio=True,
                               pos_hint={'center_x': .5, 'center_y': .3})

        self.passwordBox.add_widget(self.textinput)
        self.passwordBox.add_widget(self.passwordBox_wrong)
        self.passwordBox.add_widget(self.btn)

        def switch():
            keyboard.remove_hotkey(self.enter_hotkey)
            sm.switch_to(RapportScreen())

        # Hotkey
        self.enter_hotkey = keyboard.add_hotkey('enter', check_password, args=[self])

        # Set focus on text-input at start of screen
        self.textinput.focus = True


class RapportScreen(BgScreen):
    def __init__(self, **kwargs):
        super(RapportScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='horizontal')
        self.add_widget(self.layout)
        self.layout2 = BoxLayout(orientation='vertical', padding=[180, 80])
        self.layout.add_widget(self.layout2)
        self.layout_count = AnchorLayout(size_hint=(.9, 1))
        self.layout.add_widget(self.layout_count)

        # Start the global timer and add a Label to EscapeRoom > layout
        timer.start()
        self.timer_frame = Image(source='timer_frame.gif',
                                 anim_delay=0.05,
                                 allow_stretch=True,
                                 keep_ratio=True)
        self.layout_count.add_widget(self.timer_frame)
        self.countdown = CountdownText(text=timer.text)
        self.layout_count.add_widget(self.countdown)

        # Set the countdown-label to be equal to our global timer
        def update(dt):
            self.countdown.text = timer.text

        # Update our countdown-text every
        Clock.schedule_interval(update, 1.0 / 15.0)

        def set_focus_next(RapportScreen):
            f = focus.FocusBehavior.get_focus_next(RapportScreen)
            f.focus = True

        # Adding the layout of the entire left side
        self.agent = Label(text='DISEASE AGENT', font_size=20)
        self.agent_input = CustomTextInput(multiline=False, write_tab=False)
        self.agent_wrong = Label(text="THE DISEASE AGENT WAS INCORRECT", color=(1, 1, 1, 0))

        self.zero_name = Label(text='PATIENT ZERO NAME', font_size=20)
        self.zero_name_input = CustomTextInput(multiline=False, write_tab=False)
        self.zero_name_wrong = Label(text="PATIENT ZERO'S NAME WAS INCORRECT", color=(1, 1, 1, 0))

        self.structure = Label(text='MOLECULE STRUCTURE', font_size=40)

        self.double_bond = Label(text='DOUBLE BONDS', font_size=20)
        self.double_bond_input = CustomTextInput(multiline=False, input_type='number', write_tab=False)
        self.double_bond_wrong = Label(text="THE NUMBER OF DOUBLE BONDS IS INCORRECT", color=(1, 1, 1, 0))

        self.triple_bond = Label(text='TRIPLE BONDS', font_size=20)
        self.triple_bond_input = CustomTextInput(multiline=False, input_type='number', write_tab=False)
        self.triple_bond_wrong = Label(text="THE NUMBER OF TRIPLE BONDS IS INCORRECT", color=(1, 1, 1, 0))

        self.layout2.add_widget(self.agent)
        self.layout2.add_widget(self.agent_input)
        self.layout2.add_widget(self.agent_wrong)
        self.layout2.add_widget(self.zero_name)
        self.layout2.add_widget(self.zero_name_input)
        self.layout2.add_widget(self.zero_name_wrong)
        self.layout2.add_widget(self.structure)
        self.layout2.add_widget(self.double_bond)
        self.layout2.add_widget(self.double_bond_input)
        self.layout2.add_widget(self.double_bond_wrong)
        self.layout2.add_widget(self.triple_bond)
        self.layout2.add_widget(self.triple_bond_input)
        self.layout2.add_widget(self.triple_bond_wrong)

        # Check if info is correct. If yes, add to correct-counter, if no, show specific error message. When done counting, procced to ProgressScreen
        def check_info(RapportScreen):

            correct_answers = 0

            if self.agent_input.text.lower() == '123':
                correct_answers += 1
                self.agent_wrong.color = (1, 0, 0, 0)
            else:
                self.agent_wrong.color = (1, 0, 0, 1)

            if re.search(r'\b123\b', self.zero_name_input.text) is not None:
                correct_answers += 1
                self.zero_name_wrong.color = (1, 0, 0, 0)
            else:
                self.zero_name_wrong.color = (1, 0, 0, 1)

            if self.double_bond_input.text == '123':
                correct_answers += 1
                self.double_bond_wrong.color = (1, 0, 0, 0)
            else:
                self.double_bond_wrong.color = (1, 0, 0, 1)

            if self.triple_bond_input.text == '123':
                correct_answers += 1
                self.triple_bond_wrong.color = (1, 0, 0, 0)
            else:
                self.triple_bond_wrong.color = (1, 0, 0, 1)

            sm.add_widget(ProgressScreen(name='progress', a=correct_answers))
            sm.current = 'progress'

        # Add check-button
        self.check_button = ImageButton(on_press=check_info)
        self.layout2.add_widget(self.check_button)

        # Switch focus on enter. If at the end of screen, check info
        self.agent_input.bind(on_text_validate=set_focus_next)
        self.zero_name_input.bind(on_text_validate=set_focus_next)
        self.double_bond_input.bind(on_text_validate=set_focus_next)
        self.triple_bond_input.bind(on_text_validate=check_info)


class ProgressScreen(BgScreen):
    a = NumericProperty(0)

    def __init__(self, **kwargs):
        super(ProgressScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=[350, 300])
        self.add_widget(self.layout)

        # If NOT all answers are correct, go to previous screen, and remove self. If all ARE correct, stop timer and go to EndVideoScreen.
        def switch():
            if self.a < 4:
                sm.current = sm.previous()
                sm.remove_widget(self)
            else:
                timer.stop()
                sm.switch_to(EndVideoScreen())

        self.calculating = Label(text='CALCULATING', color=(1, 1, 1, 1), font_size=40,
                                 font_name='./Orbitron/V-GERB(bold).ttf')
        self.layout.add_widget(self.calculating)

        # Animate calculating text (Calculating -> Calculating. -> Calculating.. -> Calculating...)
        def calc_anim(RapportScreen):
            t = self.calculating.text
            if '...' in t:
                self.calculating.text = 'CALCULATING'
            else:
                self.calculating.text = t + '.'

        Clock.schedule_interval(calc_anim, 1.0 / 2.0)

        # Add animated progressbar
        self.progressBar = CustomProgressBar(switch, a=self.a)
        self.layout.add_widget(self.progressBar)


class EndVideoScreen(Screen):
    def __init__(self, **kwargs):
        super(EndVideoScreen, self).__init__(**kwargs)
        self.video = Video(source='test.mkv', state='stop')

        # Specific function that switches to EscapeRoom screen
        def switch(self, kwargs):
            sm.switch_to(WinScreen())

        # Bind a callback to eos event. Eos is when the video ends
        self.video.bind(eos=switch)
        self.add_widget(self.video)

    # When the screen enters view, play the video
    def on_enter(self, *args):
        self.video.state = 'play'


class WinScreen(BgScreen):
    def __init__(self, **kwargs):
        super(WinScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.winText = Label(text='CONGRATULATIONS\n\nTHE CURE IS MIXED\n\nTIME: ' + timer.text, font_size=70,
                             halign='center')
        self.add_widget(self.layout)
        self.add_widget(self.winText)

        # led.blink(5, 5, 1)

        # Reset timer and go to start screen
        def restart():
            keyboard.remove_hotkey(self.hotkey)
            timer.a = 3600
            sm.switch_to(IntroLogo())

        # Add custom KeyBoardListener that triggers the switch-function on enter-key
        self.hotkey = keyboard.add_hotkey('ctrl+shift+r', restart)


class FailScreen(BgScreen):
    def __init__(self, **kwargs):
        super(FailScreen, self).__init__(**kwargs)
        self.layout = FloatLayout()
        self.failText = Label(text='YOU LOSE\n\nTIME IS UP\n\n' + timer.text, font_size=70, halign='center')
        self.add_widget(self.layout)
        self.add_widget(self.failText)

        # led.blink(5, 5, 1)

        def restart():
            keyboard.remove_hotkey(self.hotkey)
            timer.a = 3600
            sm.switch_to(IntroLogo())

        # Add custom KeyBoardListener that triggers the switch-function on enter-key
        self.hotkey = keyboard.add_hotkey('ctrl+shift+r', restart)


def fail_switch():
    sm.switch_to(FailScreen())


# Setup Raspberry GPIO output
# global led
# led = LED(11)

# Add a global timer, that keeps track of the countdown between Screens
global timer
timer = CountdownTimer(fail_switch)

# Add a screen manager and a starting screen. Remove Transition-animations
sm = ScreenManager()
sm.transition = NoTransition()
sm.add_widget(IntroLogo())


class Main(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Main().run()
