# Chronic Live Streamer Addiction Simulator
#### You can now know how it feels to be addicted to live streamers.
#### Because of what this program does, I would personally consider it malware, so dont go around trolling your poor technologically inept friends with it.

# Features
 - Whenever your favourite streamer is live, whatever you are doing is shutdown and you are brought straight to the streamer's twitch page.
 - Your thoughts are projected to you in the form of TTS messages, even when the streamer isn't live.
 - You can set COWARDESS MODE on line 12 to True to make programs minimize instead of fully closing. This choice may be reflected in your thoughts though.
 - Change the user variable on line 13 to the username of the streamer you are addicted to. (Grab it from the URL of the streamers page or else it may not work!)

# Technical Details
#### The code checks if the user is live, speaks TTS messages, and closes the program in focus, every 15 seconds. This can be changed on line 23.
#### If the streamer's browser tab is in focus, then it will not be closed.
#### The code force closes the program in focus, which means Alt F4 resistent programs like CS:GO will still be forced to shutdown.
#### People with unicode in their nickname should still function as normal, although as far as I know non-ascii characters aren't spoken. This could likely be fixed by changing the engine language, but that's on you.
#### The file has a pyw extension so you'll need to shut down python with task manager within 15 seconds, or change the file to a py extension.

# Required Setup
#### The program was written for Python 3.10, but will probably still work on some other versions.
#### Some non-standard modules were used, and will need to be installed with the following commands:
 - pip install pywin32
 - pip install pypiwin32
 - pip install requests
 - pip install pyttsx3
#### I probably missed one so if you get an error relating to a missing module (or anything really,) let me know.
#### If you want to send the program to someone who doesn't have python or the required modules installed (Please make sure they know what it is they are running!), you can probably compile the program with Pyinstaller, although I haven't tested this, and I will not provide instructions.
