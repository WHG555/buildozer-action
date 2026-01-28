import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

class ROwidget(App):
    def build(self):
        Window.fullscreen = 1
        self.title="title"

        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        label1 = Label(text="ROwidget")
        button1 = Button(text="Kivy")

        self.layout.add_widget(label1)
        self.layout.add_widget(button1)
        return self.layout

if __name__ == '__main__':
    ROwidget().run()
