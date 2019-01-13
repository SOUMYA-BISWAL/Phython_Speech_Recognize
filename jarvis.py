import speech_recognition as sr
import os
from playsound import playsound
import  webbrowser
import random
import pyttsx3

speech=sr.Recognizer()
greeting_dict = {'hello': 'hello', 'hi': 'hi'}
mp3_greeting_list = ['path/yes boss.mp3']

open_launch_dict = {'open': 'open', 'launch': 'launch'}
mp3_open_launch_list = ['yesboss.mp3', 'sureboss.mp3']

social_media_dict = {'facebook': 'http://www.facebook.com', 'twitter': 'http://www.twitter.com'}

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def read_voice_cmd():
    voice_text = ''
    print 'Listing...'
    with sr.Microphone() as source:
        audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as  e:
        print 'Network error'
    except sr.WaitTimeoutError:
        pass
    return voice_text

def is_valid_note(greeting_dict, voice_note):
    for key, value in greeting_dict.iteritems():
        try:
            if value== voice_note.split(' ')[0]:
                return True
                break
            else:
                return False
        except IndexError:
            pass

def is_valid_open_lunch(open_lunch_dict, voice_note):
    for key, value in greeting_dict.iteritems():
        if value== voice_note.split(' ')[0]:
            return True
            break
        elif value== voice_note.split(' ')[1]:
            return True
            break
    return False


def speak(message):
    engine=pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-10)
    engine.say(format(message))
    engine.runAndWait()


if __name__ == '__main__':
    #playsound('C:\Users\Soumya\PycharmProjects\untitled\hello boss i am chiti artificial intelligence.mp3')
    speak("Hi boss This is your Artificial intelligence chiti")

    while True:
        voice_note = read_voice_cmd().lower()
        print 'cmd: {}'.format(voice_note)

        if is_valid_note(greeting_dict, voice_note):
            print 'In Greeting......'
            play_sound(mp3_greeting_list)
            continue

        elif is_valid_note(open_launch_dict, voice_note):
            print 'In Open.......'
            #speak("Yaa sure boss ")
            play_sound(mp3_open_launch_list)
            if is_valid_note(social_media_dict,voice_note):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer c:\\"{}"'.format(voice_note.replace('open', '').replace('launch', '')))
            continue

        elif 'bye' in voice_note:
            #speck_trxt_cmd('bye boss happy to help you have a good day')
            exit()
