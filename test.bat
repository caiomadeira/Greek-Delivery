@echo off
:lol
start calc.exe
goto lol
exit

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