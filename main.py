from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from downloader import download_and_process

class DownloaderUI(BoxLayout):
    url = StringProperty("")
    platform = StringProperty("nico")
    mode = StringProperty("video")
    output = StringProperty("")

    def run_download(self):
        if not self.url.strip():
            self.output = "Please enter a URL."
            return
        result = download_and_process(self.url, self.platform, self.mode)
        self.output = result

class ViddlApp(App):
    def build(self):
        return DownloaderUI()
