
        
        
        
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
