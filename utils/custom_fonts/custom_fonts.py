from kivymd.font_definitions import theme_font_styles
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.banner import MDBanner
from kivy.core.text import LabelBase


class CustomFonts:

    @staticmethod
    def register(name: str, path: str, theme_cls, default_size: int = None):
        LabelBase.register(name=name, fn_regular=path)
        theme_font_styles.append(name)
        if default_size is None:
            theme_cls.font_styles[name] = [name, 16, False, 0.15]
        else:
            theme_cls.font_styles[name] = [name, default_size, False, 0.15]

    def setup_fonts(self, theme_cls):
        self.register(name="GelioFasolada",
                      path="C:/Users/Caio Madeira/Desktop/GreekDelivery/resources/fonts/Gelio-Fasolada.ttf",
                      theme_cls=theme_cls)

        self.register(name="GreekSymbols",
                      path="C:/Users/Caio Madeira/Desktop/GreekDelivery/resources/fonts/greek.ttf",
                      theme_cls=theme_cls)
