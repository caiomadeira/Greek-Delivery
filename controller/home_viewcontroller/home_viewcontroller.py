from kivymd.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivymd.font_definitions import theme_font_styles
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.banner import MDBanner
from kivy.core.text import LabelBase
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.button import MDRaisedButton

from utils.custom_fonts.custom_fonts import CustomFonts

KV = """
Screen:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "C:/Users/Caio Madeira/Desktop/GreekDelivery/resources/assets/bg_app_light.png"
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'GreekDelivery'
            left_action_items: [["menu", lambda x: x]]
            
        MDSwitch:
            pos_hint: {'center_x': .9, 'center_y': .8}
            active: False
            on_active: app.setup_theme_style(self.active)
            
        HomeView:
        
<HomeCard>:
    id: home_card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    
    MDBoxLayout:
        padding: [25, 0, 25, 0]
        size_hint_y: .2
        md_bg_color: app.theme_cls.primary_color
        
        MDLabel:
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            text: 'Sobre'
    
    MDFloatLayout:
        MDLabel:
            text: 'Created by Caio Madeira'
            pos_hint: {'center_x': .5, 'center_y': .5}
            halign: 'center'
            
        MDLabel:
            text: 'GitHub: github.com/CaioMadeira'
            pos_hint: {'center_x': .5, 'center_y': .4}
            halign: 'center'
            
        MDRaisedButton:
            size_hint_x: .9
            text: 'Close'
            pos_hint: {'center_x': .5, 'center_y': .2}
            on_release: root.close_card()
        
<HomeView>:

    MDLabel:
        font_style: 'GelioFasolada'
        font_size: '70sp'
        
        halign: 'center'
        text: 'Greek Delivery'
        pos_hint: {'center_x': .5, 'center_y': .9}
    
    ButtonFocusBehavior:
        focus_color: 
        size_hint_x: .9
        size_hint_x: .5
        text: 'Hide some Text'
        pos_hint: {'center_x': .5, 'center_y': .5}
    
    MDRaisedButton:
        size_hint_x: .9
        size_hint_x: .5
        text: 'Hide some Image'
        pos_hint: {'center_x': .5, 'center_y': .4}
    
    MDRaisedButton:
        size_hint_x: .9
        size_hint_x: .5
        text: 'Hide some File'
        pos_hint: {'center_x': .5, 'center_y': .3}
    
    MDTextButton:
        text: '@Caio Madeira'
        pos_hint: {'center_x': .5, 'center_y': .1}
        on_release: root.home_opencard()
"""


class ButtonFocusBehavior(MDRaisedButton, FocusBehavior):
    pass


class HomeCard(MDCard):
    def close_card(self):
        self.parent.remove_widget(self)


class HomeView(FloatLayout):
    def home_opencard(self):
        self.add_widget(HomeCard())


class HomeViewController(MDApp):

    def setup_theme(self):
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.primary_hue = '900'

    def setup_theme_style(self, state):
        if state:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def build(self):
        self.setup_theme()
        CustomFonts().setup_fonts(theme_cls=self.theme_cls)

        return Builder.load_string(KV)


if __name__ == '__main__':
    HomeViewController().run()
