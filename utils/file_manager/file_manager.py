from kivymd.toast import toast
from kivymd.uix.filemanager import MDFileManager


class FileManager:

    def setup_file_manager(self):
        self.manager_open = False
        self.file_manager = MDFileManager(exit_manager=self.exit_manager,
                                          select_path=self.select_path,
                                          preview=True)

    def file_manager_open(self):
        path = '/'
        self.file_manager.show(path)

    def select_path(self, path):
        self.exit_manager()
        toast(path)
        print(path)
        return path

    def exit_manager(self, *args):
        self.manager_open = True
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True