from kivymd.font_definitions import theme_font_styles
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.banner import MDBanner
from kivy.core.text import LabelBase


class CustomFonts:
    def setup_fonts(self, theme_cls):
        LabelBase.register(
            name="GelioFasolada",
            fn_regular="C:/Users/Caio Madeira/Desktop/GreekDelivery/resources/fonts/Gelio-Fasolada.ttf"
        )
        theme_font_styles.append('GelioFasolada')
        theme_cls.font_styles["GelioFasolada"] = ["GelioFasolada", 16, False, 0.15]
