# --------------------------------- Exercise - 9 : Akhbaar Padhke Sunaao  ----------------------------------------------

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__" :
    import requests
    import json
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=0c79803330614437beab164cce0a28e6"
    r = requests.get(url)
    R= r.text
    s = json.loads(R)
    i = 1
    while(i<= 19):
        speak(f"{i} number of news is")
        print(s['articles'][i]['title'])
        speak(s['articles'][i]['title'])
        i += 1
    speak("That is for today. see you next day with some greatest headlines.")



# ---------------------------- OTHER WAY -----------------------------------------------------------------------------

'''
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__" :
    import requests
    import json
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=0c79803330614437beab164cce0a28e6"
    r = requests.get(url).text
    s = json.loads(r)
    speak("News for today.... Lets begin")
    a = s['articles']
    for i in  a :
        print(i['title'])
        speak(i['title'])
        speak("Moving to the next news....")
    speak("That is for today. see you next day with some greatest headlines...")
    
'''




# --------------------------------------------------------------------------------------------------------------------


