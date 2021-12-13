from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class NavigationControl(ScreenManager):
    def __init__(self, **kwargs):
        super(NavigationControl, self).__init__(**kwargs)
