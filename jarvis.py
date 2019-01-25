# WELCOME TO ========================================================================================================== JARVIS 
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
import sys
import time
import pyttsx
import tkinter as tk
import ImageGrab


INFO = '''
        *=======================================*
        |....JARVISE ARTIFICIAL INTELLIGENCE....|
        +---------------------------------------+
        |#Author: Soumya Ranjan Biswal          |
        |#Date: 01/06/2018                      |
        *=======================================*
        '''
print(INFO)

#speech contain like audio
speech = sr.Recognizer()

#all variable declaration
mp3_greeting_list = ['hiboss.mp3', 'helloboss.mp3']
mp3_open_launch_list = ['yesboss.mp3', 'sureboss.mp3']
mp3_howareyou_list = ['how_are_you.mp3', 'how_are_you1.mp3', 'how_are_you4.mp3']
mp3_thanks_list = ['have_a_niceday.mp3', 'thanks.mp3']
joke_list =['engjoke1.mp3', 'engjoke2.mp3', 'engjoke3.mp3', 'joke1.mp3', 'joke2.mp3', 'joke3.mp3', 'joke4.mp3']
mp3_whatareyoudoing_list = ['what_are_you_doing.mp3', 'what_are_you_doing2.mp3']
static_remind_speech = 'alright, i will remind '
remind_speech=''

#JARVIS'S TALK  ========================================================================================================== SENSITIVE BRAIN 
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

# JARVIS'S EARS========================================================================================================== SENSITIVE BRAIN 
def read_voice_cmd():
    voice_text = ''
    print 'Listing...'
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print 'Network error'
    except sr.WaitTimeoutError:
        pass
    return voice_text

#Text to audio Speech
def static_speech(text):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


# POLITE JARVIS ============================================================================================================= BRAIN 1   
def call_jarvis():
    while True:
        playsound('hellojarvis.mp3')
        voice_note = read_voice_cmd().lower()
        print 'cmd: {}', voice_note

        #Hi/Hello logic
        if 'hi' in voice_note or 'hello' in voice_note:
            print 'In Greeting......'
            play_sound(mp3_greeting_list)

        #Facebook open   
        elif 'open facebook' in voice_note:
            play_sound(mp3_open_launch_list)
            print 'In Open.......'
            webbrowser.open("http://www.facebook.com")

        #Youtube open    
        elif 'open youtube' in voice_note:
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            webbrowser.open("http://www.Youtube.com")

        #Open Twitter    
        elif 'open twitter' in voice_note ':
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            webbrowser.open("http://www.twitter.com")

        #Open Gmail    
        elif 'open gmail' in voice_note :
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        
        #ScrrenShot
        elif 'screenshot' in voice_note :
            print 'Taking Screenshot.......'
            name=random.randint(1000,300000)
            time.sleep(2)
            ImageGrab.grab().save("screenshot"+str(name),"JPEG")
            static_speech("Screenshot saved at "+name)
        
        #Follow Repeate with me
        elif 'Follow me' in voice_note or 'Repeate' in voice_note:
            print 'Ok Sir......'
            while True:
                with sr.Microphone() as source:
                    speech.adjust_for_ambient_noise(source)
                    repeate_audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)
                    if 'stop Repeate' in repeate_audio :
                        break
                    else:
                        static_speech(repeate_audio)
           
        #Ask Marray
        elif 'marry' in voice_note or 'will you marry' in voice_note :
            print 'NO......'
            static_speech('I am sorry.. The person you are trying to contact is currently unavailable, please try again later or join the queue for your turn')
        
        #How are you Jarvis
        elif voice_note == 'how are you' or voice_note == 'how are you jarvis':
            print 'i am fine.......'
            play_sound(mp3_howareyou_list)

        #What are you Doing    
        elif 'doing' in voice_note  or 'doing jarvis' in voice_note:
            print 'waiting for you.......'
            play_sound(mp3_whatareyoudoing_list)
          
        #GitHub Code
        elif 'code' in voice_note or 'your code' in voice_note:
            print 'Hold on.......'
            static_speech('Hold on boss I will open my code for you')
            url = ("https://github.com/SOUMYA-BISWAL/Phython_Speech_Recognize/blob/master/jarvis.py")
            webbrowser.open(url,new=new)  

        #Open Drives    
        elif 'drive' in voice_note:
            print 'In Open.......'
            play_sound(mp3_open_launch_list)
            drive= voice_note[5]
            os.system('explorer '+drive+':\\'.format(''))
            print 'ok done'
            with sr.Microphone() as source:
                speech.adjust_for_ambient_noise(source)
                drive_audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)
                if 'open' in drive_audio :
                    print 'In Open.......'
                    play_sound(mp3_open_launch_list)
                    os_note = drive_audio.replace('open ', '')
                    os.system('explorer '+drive+':\\'+os_note.format(''))   
                else:
	                break
                        

        #For Joke        
        elif 'joke' in voice_note:
            print 'ok listen.......'
            play_sound(joke_list)
            time.sleep(3)
            
        #Asking about Time    
        elif 'time' in voice_note:
            current_Time = time.strftime("%d:%B:%Y:%A")
            print current_Time
            static_speech(current_Time)
            
        #Remind command    
        elif 'remind' in voice_note :
            static_speech('what should i remind?')
            print 'ok.......'
            with sr.Microphone() as source:
                speech.adjust_for_ambient_noise(source)
                print 'say'
                audio = speech.listen(source=source, timeout=10, phrase_time_limit=3)
                global remind_speech
                remind_speech = speech.recognize_google(audio)
                static_speech(static_remind_speech+remind_speech)

        #Ask Reminder        
        elif 'reminder' in voice_note :
            print 'ok this is your reminder .......'
            if remind_speech == '':
                static_speech('you do not have any reminder for today')
            else:
                static_speech('you have one reminder' + remind_speech)

        #Thanks        
        elif 'thanks' in voice_note or 'thank you' in voice_note' :
            play_sound(mp3_thanks_list)
            print 'Thanks boss'
            jarvis_frontend()
            #pass
            #sys.exit()

        else:
           # playsound('internet.mp3')
            webbrowser.open(voice_note)
            

# JARVIS FRONTEND ========================================================================================================== SENSITIVE BRAIN             
def jarvis_frontend():
    root=tk.Tk()
    frame=tk.Frame(root)
    frame.pack()
    root.title("JARVIS")
    root.iconbitmap('C:/micro.png')
    root.geometry("235x200")
    root.config(background='blue')
    #background_image = tk.PhotoImage(file="C:/mid.gif")
    #background = tk.Label(root, image=background_image, bd=0)
    #background.pack()
    #textArea = tk.Text(root, height=5, width=29)
    #textArea.insert(root)
    #textArea.pack()
    recordBootton = tk.Button(frame,command=call_jarvis())
    photo1=tk.PhotoImage(file="C:/micro.png")
    recordBootton.config(image=photo1,width="60",height="60")
    recordBootton.pack(side=tk.LEFT)
    exitButton = tk.Button(frame,command=quit)
    photo2=tk.PhotoImage(file="C:/quit.png")
    exitButton.config(image=photo2,width="60",height="60")
    exitButton.pack(side=tk.RIGHT)
    root.mainloop()

	
	
# MAIN METHOD========================================================================================================== BRAIN     
if __name__ == '__main__':
        jarvis_frontend()

