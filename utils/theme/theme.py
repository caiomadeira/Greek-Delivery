from kivymd.uix.selectioncontrol import MDSwitch


class Theme:
    def __init__(self):
        self.primary_hue = '900'
        self.accent_hue = '400'
        self.primary = 'Brown'
        self.accent = 'Amber'

    def setup_theme(self, theme_cls):
        theme_cls.primary_palette = 'Brown'
        theme_cls.accent_palette = 'Amber'
        theme_cls.primary_hue = '900'
        theme_cls.accent_hue = '400'

