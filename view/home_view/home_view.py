import kivy

from view.navigation_control.navigation_control import NavigationControl

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class HomeView(Screen):
    def __init__(self, **kwargs):
        super(HomeView, self).__init__(**kwargs)
        self.add_widget(Image(source='resources/assets/logo_1.png'))

        # self.filename_1 = TextInput(multiline=False)
        # self.window.add_widget(self.filename_1)
        self.option_1 = Button(text="Hide Text in JPEG/JPG", size_hint=(.9, .2), pos_hint={'center_x': .5, 'y': .03},
                               bold=True, background_color='#CE9B67')
        self.add_widget(self.option_1)

        self.option_1.bind(on_press=self.screen_transition)

    def screen_transition(self, *args):
        self.manager.current = 'hide_text'
