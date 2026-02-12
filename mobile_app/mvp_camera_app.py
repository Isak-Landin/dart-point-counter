# main.py
from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import platform

# Android runtime permission + portrait lock
if platform == "android":
    from android.permissions import request_permissions, Permission
    from jnius import autoclass

class CameraApp(App):
    def build(self):
        # Android: request permission + force portrait
        if platform == "android":
            request_permissions([Permission.CAMERA])

            PythonActivity = autoclass("org.kivy.android.PythonActivity")
            ActivityInfo = autoclass("android.content.pm.ActivityInfo")
            activity = PythonActivity.mActivity
            activity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_PORTRAIT)

        root = BoxLayout(orientation="vertical")

        self.camera = Camera(play=False)
        # Fixed capture settings (best-effort; provider-dependent)
        self.camera.resolution = (1280, 720)
        self.camera.fps = 24

        controls = BoxLayout(size_hint_y=None, height="56dp")
        self.btn_toggle = Button(text="Start Camera")
        self.btn_toggle.bind(on_release=self.toggle_camera)
        controls.add_widget(self.btn_toggle)

        root.add_widget(self.camera)
        root.add_widget(controls)
        return root

    def toggle_camera(self, *_):
        self.camera.play = not self.camera.play
        self.btn_toggle.text = "Stop Camera" if self.camera.play else "Start Camera"

if __name__ == "__main__":
    CameraApp().run()
