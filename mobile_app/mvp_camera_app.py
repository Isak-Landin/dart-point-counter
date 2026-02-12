# main.py
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout

class CameraApp(App):
    def build(self):
        layout = BoxLayout()
        self.camera = Camera(play=True)
        layout.add_widget(self.camera)
        return layout

if __name__ == "__main__":
    CameraApp().run()
