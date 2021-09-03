try : 
 import pyttsx3
 import speech_recognition as sr
 import sys
 import datetime
 import threading 
 import os
 import webbrowser
 import wikipedia
 import bs4
 from bs4 import BeautifulSoup
 import requests
 import time
except Exception as e:
    print(e)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 150)

start_time = time.time()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def speak_setup(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning sir! ")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    api =  "https://www.google.co.in/search?q=temperature+in+Varanasi"
    r = requests.get(api)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div",class_="BNeawe").text
    speak("The Temperature In Varanasi is") 
    speak(temp)
    api2 ="https://www.google.com/search?q=time+in+varansi"
    r =  requests.get(api2)
    data = BeautifulSoup(r.text, "html.parser")
    time = data.find("div",class_="BNeawe").text
    speak("The Time In India Is")
    speak(time)


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
        print("Jarvis : Listing to you ")
        audio = r.listen(source, phrase_time_limit=2)
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
def TaskExe():
    while (True):

        queery = takeCommand().lower()

        if 'wikipedia' in queery:
            speak('Searching Wikipedia...')
            queery = queery.replace("wikipedia", "")
            results = wikipedia.summary(queery, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open class' in queery :
            webbrowser.open("https://classroom.google.com/u/0/h")
            speak("here you  go sir")
            
        
        elif 'tell me' in queery:
            speak('Sir i am serching on my database')
            queery = queery.replace("tell me", "")
            results = wikipedia.summary(queery, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'time' in queery:
            print(datetime.datetime.now().strftime(
                '%H hours %M minutes and %S seconds'))
            speak(datetime.datetime.now().strftime(
                '%H hours %M minutes and %S seconds'))
        elif 'break' in queery:
            speak('Ok Sir Leaving The Network for now call  me when  need')
            break
        elif 'hello' in queery:
            speak("Hello  sir")
        elif 'news' in queery:
            from Database.News.News import speak_news
            speak_news()
        elif ' live' in queery:
             webbrowser.open("https://www.youtube.com/watch?v=WB-y7_ymPJ4")
             speak("Here you go sir")
        elif 'fun'in queery :
            webbrowser.open("https://www.youtube.com/watch?v=cx3vneZyirg")
            speak("here you go sir")
        elif 'raat' in queery :
            webbrowser.open("https://www.youtube.com/watch?v=Dt5GMToSu5I")
        elif  'Code' in queery :
            os.open("")
        
        
        
        
        
        elif 'computer' in queery:
            from ComputerVesion import FaceFinder
            FaceFinder()
            speak("COMPUTER VESION  HAS BEEN  LAUNCHED WAITING FOR NEXT ODER SIR")
        elif 'back' in queery:
            speak("WELCOME BACK  SIR !")
        elif 'yes' in queery:
         speak(" Great")
        elif 'Thank' in queery:
            speak("YOUR welcome Sir!")
        elif 'world info' in queery:
         year = int(datetime.datetime.now().year)
         month = int(datetime.datetime.now().month)
         date = int(datetime.datetime.now().day)
         speak("The current date is")
         speak(date)
         speak(month)
         speak(year)
        
       
       
       
        elif 'new work' in queery: 
            from  Database.Works.Work import Crig4c
            Crig()
        
        elif 'left work' in queery: 
            from  Database.Works.Work import Crig
            
            Crig()
def core():
    try :
     while True:

        queery = takeCommand()
        
        if  'play ' in queery :
            os.startfile('b')
            speak("here you go")
        elif 'something else' in queery:
            os.startfile('')
            speak("here you  go  sir")
        
        elif 'no jarvis' in queery:
            speak("Then what shoud i  play sir")
        
        elif 'cool' in queery:
            speak("Ok playing some cool song")
            os.start('')
        
        elif 'romantic' in queery:
            speak("Ok sir playing romantic song")
            os.startfile('')
        
        elif 'funny ' in queery: 
            speak("Ok playing Some funny song")
            os.startfile('')
        
    
        elif 'last time' in queery:
            os.startfile('b')

    except Exception as e:
        print(e)

def __init__():
    import pywhatkit
   
    while (True):
     line=takeCommand()
     if 'play song' in line :
        speak("Tell me the name of the song sir ")
     commandvoice = takeCommand()
     pywhatkit.playonyt(commandvoice)
if __name__ == "__main__":
    while True :
        Pemit  = takeCommand()
        if 'wake up' in Pemit :
         speak("finally waked up")
         wishMe()

         TaskExe()
         core()
         __init__()
        
        elif 'out' in Pemit:
            speak("Ok going out for now sit call me any time")
            sys.exit()


   


print (time.time() - start_time, "seconds")


    

 







