from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_string("""

<MyTabbedPanel>:
    #size_hint: .9, .9
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
        text:"Register Tab"
        GridLayout:
            cols:2
            Label:
                text: "Name"
                size_hint:(.2, .1)
                #pos_hint:{'x':.2, 'y':.75}

            TextInput:
                size_hint:(.4, .1)
                pos_hint:{'x':.3, 'y':.65}

            Label:
                text:"Email"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.55}

            TextInput:
                size_hint:(.4, .1)
                pos_hint:{'x':.3, 'y':.45}

            Label:
                text:"Password"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.35}

            TextInput:
                password:True
                size_hint:(.4, .1)
                pos:(400, 150)
                pos_hint:{'x':.3, 'y':.25}

            Button:
                text:'Register'
                size_hint : (.2, .1)
                pos_hint : {'center_x':.5, 'center_y':.09}

    TabbedPanelItem:
        text:'Login Tab'
        GridLayout:
            cols:2
            Label:
                text:"Email"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.55}

            TextInput:
                size_hint:(.4, .1)
                pos_hint:{'x':.3, 'y':.45}

            Label:
                text:"Password"
                size_hint:(.2, .1)
                pos_hint:{'x':.2, 'y':.35}

            TextInput:
                password:True
                size_hint:(.4, .1)
                pos:(400, 150)
                pos_hint:{'x':.3, 'y':.25}

            Button:
                text:'Login'
                size_hint : (.2, .1)
                pos_hint : {'center_x':.5, 'center_y':.09}

""")


Window.size = (720,300)

class MyTabbedPanel(TabbedPanel):
    pass

class TabbedPanelApp(App):
    def build(self):
        return MyTabbedPanel()


if __name__ == '__main__':
    TabbedPanelApp().run()
