import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as source:
    print ("what you want to Print: ")
    audio = r.listen(source)

# print ("You are Saying: " + r.recognize_google(audio))

p = r.recognize_google(audio)
webbrowser.open(p)
