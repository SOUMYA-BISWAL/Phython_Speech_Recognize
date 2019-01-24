
        
        
        
//browse

elif ('google search') in response :
        query = response
        stopwords = ['google', 'search']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        webbrowser.get(Chrome).open('https://www.google.com/search?sourceid=chrome&ie=utf-8&oe=utf-8&aq=t&hl=&q='+result)
    elif ('google maps') in response:
        query = response
        stopwords = ['google', 'maps']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)
        Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
        webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")

        
//extra

elif('will you marry me') in response:
        print('I am sorry.. The person you are trying to contact is currently unavailable, please try again later or join the queue for your turn')
    elif('what is life') in response :
        print("Food")
    elif 'open email' in response:
        if mail==1:
            webbrowser.open(email)
            print ('Opening mail')
        else:
            esite=input('What email site do you use: ')
            if 'gmail' in response:
                mail=1
                email='https://www.gmail.com'
                webbrowser.open(email)
            elif 'yahoo' in response:
                mail=1
                email='https://mail.yahoo.com'
                webbrowser.open(email)
            elif 'outlook' in response:
                mail=1
                email='https://outlook.live.com'
                webbrowser.open(email)

//time and qs
    elif response == ("what is your favorite color"):
        print("purple")
    elif response == ("who are you"):
        print ("jarvia")
    elif response == "what are you":
        print ("an AI")
    elif response == ("cool"):
        print ("mhm")
    elif ('what can you do') in response:
        rand = ('I can do Tasks as Playing Music, Videos, Opening any file, websites,Google Search,Movie Search, Put Computer to sleep, Arithmatic Operations, Normal Conversations, Jokes and many more')
    





///new

elif('what is my location') in response or ('where am I') in response or ('where are you') in response :
        w = requests.get('http://api.openweathermap.org/data/2.5/weather?id=1275004&appid=5fc29900336d19d1d912723dc3d1e117')
        json_object = w.json()
        loc_lon = (float(json_object['coord']['lon']))
        rand1 = str(loc_lon)
        loc_lat = (float(json_object['coord']['lat']))
        rand2 = str(loc_lat)
        print("The current position is "+rand1+" longitude and "+rand2+" latitude")
