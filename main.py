import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.properties import ObjectProperty


class Container(BoxLayout):
    pass


class My(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    My().run()
