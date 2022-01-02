import io
import time

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
from kivymd.uix.boxlayout import BoxLayout
from utils.custom_fonts.custom_fonts import CustomFonts
# from utils.file_manager.file_manager import FileManager
from viewmodel.hidetext_viewmodel import HideTextViewModel
from kivy.lang.builder import Builder
from plyer import filechooser

from kivymd.uix.textfield import MDTextFieldRound, MDTextField


# Option 1 Screen
class HideTextView(Screen):
    def file_chooser(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        text_to_hide = self.ids.hide_text_field.text
        if selection:
            self.ids.selected_path.text = selection[0]
            time.sleep(2)
            if text_to_hide:
                self.encrypt_text(filename=selection[0], text=text_to_hide)
                time.sleep(1)
                self.result_labels(flag=True)
            else:
                self.ids.hide_text_field.helper_text = "Você precisa digitar algum texto."
                self.result_labels(flag=False)
        else:
            self.ids.selected_path.text = "Nenhum arquivo escolhido."
            self.result_labels(flag=False)

    def encrypt_text(self, filename, text):
        with open(str(filename), 'ab') as f:
            f.write(str.encode(text))

    def result_labels(self, flag: bool):
        if flag:
            self.ids.result_label.text = "Texto escondido com sucesso!"
        elif not flag:
            self.ids.result_label.text = "Não foi possível esconder o texto."
            self.ids.selected_path.text = ""
        else:
            self.ids.result_label.text = ""


# Option 2 Screen
async def loading():
    pass


class HideImageView(Screen):
    def file_chooser_2(self):
        filechooser.open_file(on_selection=self.selected_2)

    def selected_2(self, selection):
        img_to_hide = self.ids.selected_img.text
        if selection:
            self.ids.img_selected_label.text = selection[0]
            self.ids.img_preview.source = selection[0]
            time.sleep(2)


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

