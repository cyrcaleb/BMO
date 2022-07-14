import speech_recognition as sr  #microphone speech recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from time import gmtime, strftime
import threading as th
import pyjokes
import winsound #windows only to replay a file sound to a user

import sounddevice as sd   #record audio from microphone and store it in NumPy array
from scipy.io.wavfile import write #write onto a file

import multiprocessing


import cv2  #for video files

#imports a mp4 video and plays it without sound
# vid = cv2.VideoCapture('H:\\BMO POC\\GOFjoji.mp4')
#
# if (vid.isOpened() == False):
#     print("error...")
#
# while (vid.isOpened()):
#
#     ute, pic_fra = vid.read()
#
#     if ute == True:
#         cv2.imshow('Frame', pic_fra)
#
#         if cv2.waitKey(25) & 0xFF == ord('u'):
#             break
#
#     else:
#         break
#
# vid.release()
# cv2.destroyAllWindows()

 ########


# filename = 'GOFjoji.wav'  # Assign file name
# winsound.PlaySound(filename, winsound.SND_FILENAME) #play sound




#prints out all stereo mixers  (currently index 4 for headset speakers)
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))








#create an audio File from microphone
# fs = 44100 # Sample rate
# seconds = 5 #Duration of recording
#
# print('recording audio..')
# myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2 )
# sd.wait() # Wait until recording is finished
# write('output.wav', fs, myrecording) #save as WAV file
#######

#play a wav file back to user
# filename = 'output.wav'
# winsound.PlaySound(filename, winsound.SND_FILENAME)
#######





listener = sr.Recognizer()

# records the data from the file into an AutoData instance
# harvard = sr.AudioFile('audio_files_harvard.wav')
# with harvard as source:
#     audio = listener.record(source)
#     hAudio = listener.recognize_google(audio)
#     print(hAudio)
########


#talks back to user
engine = pyttsx3.init()  #speaks to user
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)  #changes voices

# prints valid voice channels
# for voice in voices:
#     print(voice, voice.id)
#     engine.setProperty('voice', voice.id)
#     engine.say("Hello World!")
#     engine.runAndWait()
#     engine.stop()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    #engine.say("Where is Fin and Jake")
    #engine.runAndWait()  #runs the rest of the program
#########

def take_command():

    # gets audio from user microphone and print out what they said
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "bmo" in command:
                if 'bmo' in command:
                    command = command.replace('bmo ', '') #takes out bmo for google seraches
                if 'hey' in command:
                    command = command.replace('hey', '')
                if 'pay' in command:
                    command = command.replace('pay', '')
                print(command) #i can comment this out once I am finished
                talk(command)  #i can comment this out once I am finished
    except:
        run_alexa()
    return command




def run_alexa():

    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
        run_alexa()
    elif 'search' in command:
        search = command.replace('search ', '')
        pywhatkit.search(search)
        run_alexa()
    elif 'date' in command:
        date = strftime("%a, %d %b %Y") #gets weekday, Day, month, and year
        talk("Today's Date is " + date)
    elif 'timer' in command:
        timer = command.replace('set', '')
        timer = timer.replace(' a ', '')
        timer = timer.replace('timer', '')
        timer = timer.replace('for', '')
        timer = timer.replace('to', '')
        holder = timer

        print("Timer is set to " + holder)
        talk("Timer is set to " + holder)


        seconds = holder.replace('hours', '')
        seconds = seconds.replace('hour', '')
        seconds = seconds.replace('minutes', '')
        seconds = seconds.replace('minute', '')
        seconds = seconds.replace('and', '')
        seconds = seconds.replace('seconds', '')
        secondsArr = seconds.split(' ')
        print(secondsArr)
        if 'hour' in holder:
            i= 0
            while secondsArr[i] == '':
                i+=1
            hours = secondsArr[i]
            print("Hours = " + hours)
            secondsArr[i] = ''
            firstholder = i
        else:
            hours = 0
            firstholder = 0

        if 'minutes' in holder:
            i = firstholder+1
            while secondsArr[i] == '':
                i += 1
            minutes = secondsArr[i] + secondsArr[i+1]
            print("Minutes = " + minutes)
            secondsArr[i] = ''
            secondsArr[i+1] = ''
            secondHolder = i+1
        elif 'minute' in holder:
            i = firstholder + 1
            while secondsArr[i] == '':
                i += 1
            minutes = secondsArr[i] + secondsArr[i + 1]
            print("Minutes = " + minutes)
            secondsArr[i] = ''
            secondHolder = i
        else:
            minutes = 0
            secondHolder = 0

        i = secondHolder
        while secondsArr[i] == '':
            i += 1
        seconds = secondsArr[i]
        print("Seconds = " + seconds)

        total = int(seconds) + int(minutes)*60 + int(hours)*60*60
        print(total)

        def sctn():
            talk("BEEP BEEP BEEP.  Time is up")
        S = th.Timer(total, sctn)
        S.start()
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p') #use H instead of I for 24 hr time
        talk('Current time is ' + time)
        print(time)
        run_alexa()
    elif 'what is' or 'who is' or "what are" or "who are" in command:
        info = wikipedia.summary(command)
        print(command)
        print(info)
        talk(info)
        run_alexa()
    # elif 'tell me a joke' in command:
    #     talk(pyjokes.get_joke())
    else:
        talk('Sorry I do not know that command')
    return

while True:
    run_alexa()
