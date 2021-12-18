from kivymd.toast import toast
from descriptor.hidetext.hidetext_descriptor import HideTextDescriptor
from kivymd.uix.filemanager import MDFileManager


class HideTextViewModel:
    def __init__(self, filename, text):
        self.filename = HideTextDescriptor(filename)
        self.text = HideTextDescriptor(text)
        self.path = '/'

    def write_text(self):
        print(self.text)
        with open(self.filename, 'ab') as f:
            f.write(self.text)
