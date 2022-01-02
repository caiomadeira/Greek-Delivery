from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp


"DEBUG CELL PHONE"
Window.size = (350, 600)


kv = """
#:import KivyLexer kivy.extras.highlight.KivyLexer
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

BoxLayout:
    HotReloadViewer:
        path: app.path_to_kv_file
        erros: True
        errors_text_color: 0, 0, 0, 1
        erros_background_color: app.theme_cls.bg_dark
"""


class SplashScreen(MDApp):
    path_to_kv_file = r"C:\Users\Caio Madeira\Documents\GitHub\greek-delivery\view\splash\splash.kv"

    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    SplashScreen().run()