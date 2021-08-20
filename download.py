import urllib.request
import threading

import youtube_dl

# [1] https://www.codespeedy.com/how-to-check-the-internet-connection-in-python/
def checkOnlineActivity(host='http://google.com'):
    """ Checks if user is connected to the internet. """
    try:
        urllib.request.urlopen(host) 
        return True
    except:
        return False
      
#print( 'connected' if checkOnlineActivity() else 'no internet!')

def checkValidUrl(url):
    """ Checks if url input is valid. """
    if checkOnlineActivity() == True:
        try:
            split = url.split('/')

            if split[2] == 'www.youtube.com' or split[2] == 'youtu.be':

                print('Valid Url!')

                return True
            else:
                print("Invalid Url - Not a Youtube Url")
        except Exception:        
            print("Invalid Url")
    else:
        print('Connect to the Internet!')

def videoQuality():
    """ Select different video qualities. """
    quality = ['240p', '360p', '480p', '720p', '1080p']
    return quality[4]

def videoOptionDict():
    """ Video Download Options based on videoQuality() """
    ydl_opts = {
        'format': 'best',
        'ignoreerrors': False,
        'outtmpl':'/Downloads/%(title)s.%(ext)s'
    }
    return ydl_opts


class downloadThread(threading.Thread):
    def __init__(self,url,ydl_opts):
        threading.Thread.__init__(self)
        self.url = url
        self.ydl_opts = ydl_opts

    def run(self):
        try:
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                ydl.download([self.url])
            #downloadVideo(url)
        except SystemExit: 
            pass
        except Exception as exp:
            pass       