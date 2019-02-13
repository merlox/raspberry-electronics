import threading
from datetime import datetime
import webbrowser
import os

# Every minute check the current time and if it's between 9am and 11am open the freecodecamp music
isPlayingMusic = False
startHour = 9
endHour = 11

def startInterval():
    threading.Timer(60.0, startInterval).start()
    print('Running...')

    global isPlayingMusic

    url = 'https://www.youtube.com/watch?v=vAKtNV8KcWg'
    currentHour = datetime.now().hour

    if(currentHour >= endHour and isPlayingMusic):
        # Stop playing music
        print('Stopping music by killing youtube...')
        isPlayingMusic = False
        os.system('killall "chromium-browse"')
    elif(currentHour >= startHour and currentHour < endHour and not isPlayingMusic):
        # Play music
        print('Starting music by opening youtube...')
        isPlayingMusic = True
        webbrowser.open(url)

startInterval()
