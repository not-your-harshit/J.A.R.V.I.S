import wikipedia
import smtplib as s
import datetime
import os
import pyttsx3
import speech_recognition as sr
ERR = ['#39865 - EMAIL  DENIED ','#002312 - PAYLOAD FAIL' , '#081242 - USER NOT FOUND']
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 190)

try :
 from NotiFierPro.Notify_me_on_command import On_ai_callback , on_pasword_wrong ,on_password_true,On_email_send
except Exception as e:
    print(e)



def email_on_online():
    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()

    ob.login("100teamjarvis@gmail.com", Config_password)
    subject = "Jarvis Turned On "
    body = "Unknown user Turned on  Jarvis Programe On Server please Check Jarvis Asap !- Jarvis"

    message = "subject:{}\n\n{}".format(subject, body)
    print(message)

    deliver_email = ('100teamjarvis@gmail.com')

    ob.sendmail("100teamjarvis@gmail.com", deliver_email, message)
    On_email_send()


def email_on_wrong():
    On_email_send()
    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()

    ob.login("100teamjarvis@gmail.com", Config_password)
    subject = "Jarvis Sequrity Thread"
    body = "Unknown user Has Enterd Wrong Pasword Safety Measure Have Been Taken Sir pls Check Server - Jarvis "

    message = "subject:{}\n\n{}".format(subject, body)
    print(message)

    deliver_email = ('100teamjarvis@gmail.com')

    ob.sendmail("100teamjarvis@gmail.com", deliver_email, message)


def accese():

    ob = s.SMTP("smtp.gmail.com", 587)
    ob.starttls()

    ob.login("100teamjarvis@gmail.com", Config_password)
    subject = "Jarvis Sequrity Login"
    body = "Unknown user Has Enterd Right  Pasword Safety Measure Have Been Not Taken  - Jarvis "

    message = "subject:{}\n\n{}".format(subject, body)
    print(message)

    deliver_email = ('100teamjarvis@gmail.com', 'hs.202007@gmail.com')

    ob.sendmail("100teamjarvis@gmail.com", deliver_email, message)


accese()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def speak_setup(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'You said: {query}\n')

    except Exception as e:
        print(e)

        print('Say that again please...')
        speak('Say that again please...')

        return 'None'

    return query


def pasword_config(pass_inp):

    password = Config_password

    passs = int(Config_email)

    if passs == int(pass_inp):

        from Index import TaskExe
        on_password_true()

        speak("ACCEPTED FOR THE FILE")
        TaskExe()

        
        accese()
        try:

            speak("ACCETED")
        except Exception as e:
            print(e)
            speak("SECURITY SYESTEM HAS ",ERR(1))


    else:
        on_pasword_wrong()
        speak(" USER ACCES DENIED NOT ACCEPTED ")
        speak("SYESTEM INBUILD SECURITY ONLINE PAYLOAD ACTIVATION CONFORMED")
        speak("PAYLOAD SECURITY CONFORMED")
        speak("INBUILD LOADS SET VALUES TO DECLINED-899")
        os.startfile('pasword.mp3')
        email_on_wrong()


Question = "ENTER PASWORD :"

if __name__ == "__main__":

    speak("TO ACCEPT YOU  FOR THIS FILE YOU NEED TO CLEAR THE TEST")
    speak("CONFIGRATION SET TO HIGH PASS FILES")


    passssss = input(Question)
    On_ai_callback()
    pasword_config(passssss)
