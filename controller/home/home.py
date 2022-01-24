import io
import time
import random
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivy.uix.screenmanager import Screen, ScreenManager
from plyer import filechooser
from pathlib import Path


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


# fake door
class RevealImageView(Screen):
    def file_chooser_reveal(self):
        filechooser.open_file(on_selection=self.selected)

    def selected(self, selection):
        reveal = self.ids.selected_path_reveal.text
        if selection:
            self.ids.selected_path_reveal.text = selection[0]
            time.sleep(2)
            message = self.reveal_text(filename=selection[0])
            if message is not None:
                print(message)
                time.sleep(1)

                self.ids.reveled_message.text = message
                time.sleep(1)
                self.save_message(message=message)
                self.ids.selected_path_reveal.text = 'Message saved in text file in your user folder.'
            else:
                self.ids.reveled_message.text = "Empty."

    def reveal_text(self, filename):
        with open(filename, 'rb') as f:
            file = f.read()
            offset = file.index(bytes.fromhex("FFD9"))

            f.seek(offset + 2)
            message = str(f.read())
            if message.startswith("b'"):
                simplify = message[1:]
            return simplify

    def save_message(self, message):
        hash = random.getrandbits(128)
        home_path = Path.home()
        if message != "" or message != "Empty.":
            with open(f"{home_path}/gd_text_{str(hash)}.txt", "w+") as f:
                f.write(message)
                f.close()
        time.sleep(1)



# fake door
class FakeDoorView(Screen):
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
