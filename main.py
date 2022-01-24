"""
Caio Madeira - 2021

"""
# kivy imports
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.core.window import Window
# scenes imports
from utils.theme.theme import Theme
from utils.custom_fonts.custom_fonts import CustomFonts
from controller.home.home import HomeView, HomeCard, ButtonFocusBehavior
from kivy.config import Config
from kivy import platform
import sys

if platform == 'win' or sys.platform == 'linux2' or platform == 'macosx':
    Config.set('graphics', 'width', '5')
    Config.set('graphics', 'height', '5')
elif platform == 'ios' or platform == 'android':
    pass


class NavigationControl(ScreenManager):
    pass


class AppDelegate(MDApp, Theme):
    global sm
    sm = ScreenManager()

    def set_app_title(self):
        self.title = "Greek Delivery"

    def set_app_icon(self):
        self.icon = "resources/assets/app_icon/app_icon_1.png"

    def change_style(self, state):
        if state:
            self.theme_cls.theme_style = "Dark"

        else:
            self.theme_cls.theme_style = "Light"

    def build(self):
        self.set_app_title()
        self.set_app_icon()
        self.setup_theme(theme_cls=self.theme_cls)
        CustomFonts().setup_fonts(theme_cls=self.theme_cls)
        sm.add_widget(Builder.load_file(r'view\splash\splash.kv'))
        sm.add_widget(Builder.load_file(r'view\home\home.kv'))

        return sm

    def on_start(self):
        Clock.schedule_once(self.change_screen, 10)

    def change_screen(self, dt):
        sm.current = "main"


if __name__ == '__main__':
    AppDelegate().run()
