import win32gui as wg
import win32process as wp
import codecs
import os
import signal
import random
import webbrowser
import requests
import pyttsx3
import time

COWARDESS_MODE=False #when set to true the program will simply minimize processes instead of killing them

engine=pyttsx3.init() #initialises the tts engine
engine.setProperty('rate', 175) #makes the TTS speak a little slower

user="jerma985" #the name of the streamer you want to stalk as shown in their URL
url=requests.get("https://www.twitch.tv/"+user) #loads everything in the url
nick=(str(url.content).split('><meta name="twitter:title" content="')[1]); nick=nick.split(' - Twitch')[0]; #finds the twitch username
nick=(codecs.escape_decode(bytes(nick,"utf8"))[0].decode("utf8")) #converts unicode markers into their symbols

while True:
    time.sleep(15) #waits between checks
    url=requests.get("https://www.twitch.tv/"+user) #reloads the url to check if the user is live
    rando=random.randint(0,4) #chooses a random number to select a tts line
    if "isLiveBroadcast" in url.text: #checks if the user is live
        window=(wg.GetForegroundWindow()) #grabs the foreground window
        windowtext=(str(wg.GetWindowText(window)).split(" ")) #grabs the foreground window title and splits it

        try:windowtext=windowtext[0]+" "+windowtext[1]+" "+windowtext[2] #converts the split window title into a twitch name, just incase the user is on twitch
        except: windowtext=str(wg.GetWindowText(window)) #if it isn't twitch an error might occur, so this avoids that.

        if nick+" - Twitch"==windowtext: #if the live stream is open and the streamer is live, it will select a random phrase of joy
            if rando==0: speak="I'm so happy to be watching "+nick+" live"
            elif rando==1: speak=nick+" is so fun and interesting to watch"
            elif rando==2: speak=nick+" is really making my day right now"
            elif rando==3: speak="It is a good day when I'm watching "+nick
            elif rando==4: speak="I don't know what I would do if "+nick+" wasn't streaming"
        else: #if the live stream is not open, but the streamer is live
            if (wg.GetWindowText(window) in ("Program Manager","Search",""))==False: #it will make sure the current process is not program manager (desktop)
                if COWARDESS_MODE==False: #if the user is not a coward
                    pid=wp.GetWindowThreadProcessId(window) #it will find the window ID of the current focused program
                    os.kill(pid[-1],signal.SIGTERM) #and kill it
                    print('Killed "'+wg.GetWindowText(window)+'"')
                elif COWARDESS_MODE==True: #if the user is a coward
                    wg.CloseWindow(window) #it will minimize the program instead
                    print('Minimized"'+wg.GetWindowText(window)+'" you coward')
            webbrowser.open_new(url.url) #opens the streamer's twitch page
            if rando==0: speak="It is time to watch "+nick #selects a random phrase of preperation
            elif rando==1: speak=nick+" time"
            elif rando==2: speak=nick+" is finally back to bring joy to my life"
            elif rando==3: speak=nick+" is live, I can be happy again"
            elif rando==4: speak="My horrible day can finally be saved because "+nick+" is live"
    else: #if the streamer isn't live, then pick a random phrase of sadness
        if rando==0: speak="I really miss "+nick+" right now"
        elif rando==1: speak="I wish I were watching "+nick+" right now"
        elif rando==2: speak="I'm so lonely without "+nick+"'s streams"
        elif rando==3: speak="If only "+nick+" were streaming right now"
        elif rando==4: speak="It's hard to stay happy when "+nick+" isn't live"
    
    if COWARDESS_MODE==False: coward="" #if the user is not a coward, do nothing
    if COWARDESS_MODE==True: coward=" also I am a worthless coward" #if the user is a coward, point it out to them very clearly
    print(speak+coward)
    engine.say(speak+coward) #queues up the tts sentence
    engine.runAndWait() #tts speaks
