# mvp_camera_app.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button

class CameraApp(App):
    def build(self):
        root = BoxLayout(orientation="vertical")

        self.cam = Camera(play=True)  # this was the working path
        root.add_widget(self.cam)

        controls = BoxLayout(size_hint_y=None, height="56dp")
        btn = Button(text="Stop Camera")
        btn.bind(on_release=self.toggle_camera)
        controls.add_widget(btn)

        root.add_widget(controls)
        self.btn = btn
        return root

    def toggle_camera(self, *_):
        self.cam.play = not self.cam.play
        if self.cam.play != True:
            self.cam.disabled = True

        self.btn.text = "Stop Camera" if self.cam.play else "Start Camera"

if __name__ == "__main__":
    CameraApp().run()
