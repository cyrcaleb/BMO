import speech_recognition as sr  #microphone speech recognition
import pyttsx3

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




listener = sr.Recognizer()

#talks back to user
engine = pyttsx3.init()  #speaks to user
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  #changes voices
engine.say("Where is Fin and Jake")
engine.runAndWait()  #runs the rest of the program
#########

#create an audio File from microphone
fs = 44100 # Sample rate
seconds = 5 #Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2 )
sd.wait() # Wait until recording is finished
write('output.wav', fs, myrecording) #save as WAV file
#######

#play a wav file back to user
filename = 'output.wav'
winsound.PlaySound(filename, winsound.SND_FILENAME)
#######







# records the data from the file into an AutoData instance
# harvard = sr.AudioFile('audio_files_harvard.wav')
# with harvard as source:
#     audio = listener.record(source)
#     hAudio = listener.recognize_google(audio)
#     print(hAudio)
########

# gets audio from user microphone and print out what they said
isListening = False
try:
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "bmo" in command:
            isListening = True
            print(command)
except:
    pass



