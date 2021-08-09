from kivy.app import App
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

from download import checkOnlineActivity, checkValidUrl, videoQuality,videoOptionDict,downloadThread 

#BackGround Colour
Window.clearcolor = get_color_from_hex('#101216')

class RV(RecycleView):
    pass

class AddDownloadForm(BoxLayout):

    video_link = ObjectProperty()

    def checkVideoLink(self):
        #https://www.youtube.com/watch?v=tPEE9ZwTmy0
        checkVideoLink=checkValidUrl(url=self.video_link.text) 
        return checkVideoLink

    def start_download(self):

        ydl_opts = videoOptionDict()
        url=self.video_link.text

        download=downloadThread(url ,ydl_opts)
        download.start()

class youtubeDownload(App):
    def build(self):
        return

if __name__ == '__main__':
    youtubeDownload().run()