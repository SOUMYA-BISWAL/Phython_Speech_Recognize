# import gTTS (Google Text To Speech)

from gtts import gTTS

text=""
# read content from file 
with open("abc.txt","r") as file:
    for line in file:
        text=text+line


speech = gTTS(text)

#slow voice and english
#speech = gTTS(text,'en','slow')

speech.save("hello.mp3")
