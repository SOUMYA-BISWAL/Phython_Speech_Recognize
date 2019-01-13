import speech_recognition as sr
import pyttsx3

def speck(message):
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10)
    engine.say(format(message))
    engine.runAndWait()

# declare text and call speck function
text = "How can i help you"
speck(text)

# call package recognize function
r = sr.Recognizer()
with sr.Microphone() as source:
    print ("what you want : ")
    audio = r.listen(source)

# Print What you are Saying
print ("You are Saying: " + r.recognize_google(audio))

speck(r.recognize_google(audio))
