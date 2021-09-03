from sys import modules
import pyttsx3
import speech_recognition as sr
import json
import webbrowser
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 150)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    required = 0
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "pulse" in name:
            required = index
    r = sr.Recognizer()
    with sr.Microphone(device_index=required) as source:
        r.adjust_for_ambient_noise(source)
        print("jj Listing to you ")
        audio = r.listen(source, phrase_time_limit=1)
        r.energy_threshold = 400

    try:
        input = r.recognize_google(audio)

        print("HA4SHIT SAYS: " + input)
        return str(input)
    except sr.UnknownValueError:
        print("Jarvis is not able to recognize audio")
        speak("Sir you  are not clear pls say again")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        
        speak("Could not request results from Google Speech Recognition service; {0}".format(e))
    return 'None'  

def speak_news():
 
    url ="https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey="
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict['articles']
    speak('News Are As following')
    speak('Todays Headlines are..')
    for index, articles in enumerate(arts):
        speak(articles['title'])
        if index == len(arts)-1:
            break
        speak('Moving on the next news headline..')
    speak('These were the top headlines, Have a nice day Sir')



def getNewsUrl():
    return 'https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey='



               

            
if __name__ == '__main__':
    speak_news()
 

