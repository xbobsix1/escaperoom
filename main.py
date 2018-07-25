from kivy.app import App
from kivy.core.window import Window

from escaperoom.stage3 import EscapeRoom

class Main(App):

    global stage
    stage = 2

    # Window.fullscreen = True
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
