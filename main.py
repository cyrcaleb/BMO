import speech_recognition as sr  #microphone speech recognition
import pyttsx3
import pywhatkit
import datetime
import wikipedia
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
engine.setProperty('voice', voices[1].id)  #changes voices

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
                print(command)
                talk(command)
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
#     elif 'tell me a joke' in command:
#         talk(pyjokes.get_joke())
    else:
        talk('Sorry I do not know that command')
    return

while True:
    run_alexa()
