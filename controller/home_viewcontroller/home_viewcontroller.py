from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.card import MDCard
from kivy.clock import Clock
from kivymd.font_definitions import theme_font_styles
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.banner import MDBanner
from kivy.core.text import LabelBase
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.toast import toast
from utils.custom_fonts.custom_fonts import CustomFonts
from utils.file_manager.file_manager import FileManager
from viewmodel.hidetext_viewmodel import HideTextViewModel

from kivymd.uix.textfield import MDTextFieldRound, MDTextField

kv = """
Screen:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "C:/Users/Caio Madeira/Desktop/GreekDelivery/resources/assets/bg_app_light.png"
    MDBoxLayout:
        orientation: 'vertical'
        MDToolbar:
            padding: [25, 0, 0, 0]
            title: 'GreekDelivery'
            left_action_items: [["menu", lambda x: None]]
        NavigationControl:
            HomeView:
                name: 'home'
            HideTextView:
                name: 'hide_text'
            HideImageView:
                name: 'hide_img'

<HomeCard>:
    id: home_card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}
    
    MDBoxLayout:
        adaptive_height: True
        padding: [25, 0, 25, 0]
        size_hint_y: .2
        md_bg_color: app.theme_cls.primary_color
        
        MDLabel:
            markup: True
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
    MDSwitch:
        pos_hint: {'center_x': .9, 'center_y': .9}
        active: False
        on_active: app.setup_theme_style(self.active)
    MDLabel:
        font_style: 'GelioFasolada'
        font_size: '70sp'
        
        halign: 'center'
        text: 'Greek Delivery'
        pos_hint: {'center_x': .5, 'center_y': .9}
    
    ButtonFocusBehavior:
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
        size_hint_x: .9
        size_hint_x: .5
        text: 'Hide some Text'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: 
            root.manager.current = 'hide_text'
            root.manager.transition.direction = 'left'
    
    ButtonFocusBehavior:
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
        size_hint_x: .9
        size_hint_x: .5
        text: 'Hide some Image'
        pos_hint: {'center_x': .5, 'center_y': .4}
        on_release: 
            root.manager.current = 'hide_img'
            root.manager.transition.direction = 'left'
    
    ButtonFocusBehavior:
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
        size_hint_x: .9
        size_hint_x: .5
        text: 'Hide some File'
        pos_hint: {'center_x': .5, 'center_y': .3}
    
    MDTextButton:
        text: '@Caio Madeira'
        pos_hint: {'center_x': .5, 'center_y': .1}
        on_release: root.home_opencard()
        
<HideTextView>:
    FloatLayout:
        MDLabel:
            font_style: 'GelioFasolada'
            font_size: '70sp'
            halign: 'center'
            text: 'Greek Delivery'
            pos_hint: {'center_x': .5, 'center_y': .9}
        
        MDIconButton:
            icon: 'arrow-left-circle'
            pos_hint: {'center_x': .1, 'center_y': .9}
            on_release: 
                root.manager.current = 'home'
                root.manager.transition.direction = 'right'
            
        MDTextField:
            id: hide_text_field
            required: True
            multiline: True
            fill_color: 0, 1, 2, 1
            mode: "fill"
            max_text_length: 120
            fill_color: 0, 0, 0, .4
            size_hint_x: .5
            pos_hint: {'center_x': .5, 'center_y': .6}
            helper_text: "Ex: Hello World."
            helper_text_mode: "persistent"
            color_mode: 'accent'
            active_line: False
            error_color: 255, 255, 20, 1
        
        ButtonFocusBehavior:
            focus_color: app.theme_cls.accent_color
            unfocus_color: app.theme_cls.primary_color
            text: 'Search'
            pos_hint: {'center_x': .6, 'center_y': .4}
            on_release: app.file_manager_open()
        
        MDLabel:
            id: label_search_path
            font_size: '20sp'
            text: 'File:' 
            halign: 'center'
            pos_hint: {'center_x': .3, 'center_y': .4}
        
        MDRaisedButton:
            size_hint_x: .9
            text: 'Hide.'
            pos_hint: {'center_x': .5, 'center_y': .2}
            on_release: root.get_textfield_text()
            
<HideImageView>:
    FloatLayout:
        MDLabel:
            font_style: 'GelioFasolada'
            font_size: '70sp'
            halign: 'center'
            text: 'Greek Delivery'
            pos_hint: {'center_x': .5, 'center_y': .9}
        
        MDIconButton:
            icon: 'arrow-left-circle'
            pos_hint: {'center_x': .1, 'center_y': .9}
            on_release: 
                root.manager.current = 'home'
                root.manager.transition.direction = 'right'
                
        ButtonFocusBehavior:
            focus_color: app.theme_cls.accent_color
            unfocus_color: app.theme_cls.primary_color
            text: 'Search'
            pos_hint: {'center_x': .5, 'center_y': .7}
    
"""


# Screen Manager
class NavigationControl(ScreenManager):
    pass


# Option 1 Screen
class HideTextView(Screen, FileManager):

    def get_textfield_text(self):
        print(self.ids["hide_text_field"].text)
        return self.ids["hide_text_field"].text

    def hide_text(self):
        HideTextViewModel(filename=r'C:\Users\Caio Madeira\Desktop\GreekDelivery\GreekDelivery.jpg',
                          text=self.get_textfield_text()).write_text()


# Option 2 Screen
class HideImageView(Screen):
    pass


# Option 3 Screen
class HideFileView(Screen):
    pass


# =================================================
# Home Screen
class ButtonFocusBehavior(MDRaisedButton, FocusBehavior):
    pass


class HomeCard(MDCard):
    def close_card(self):
        self.parent.remove_widget(self)


# Main Screen
class HomeView(Screen):
    def home_opencard(self):
        self.add_widget(HomeCard())


class AppDelegate(MDApp, FileManager):
    def setup_theme(self, primary_hue, accent_hue):
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.primary_hue = primary_hue
        self.theme_cls.accent_hue = accent_hue

    def setup_theme_style(self, state):
        if state:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"

    def build(self):

        self.setup_theme(primary_hue='900', accent_hue='400')
        CustomFonts().setup_fonts(theme_cls=self.theme_cls)
        return Builder.load_string(kv)
