import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)
engine.setProperty('rate', 140)


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
        print("Say something!")
        audio = r.listen(source, phrase_time_limit=4)
        r.energy_threshold = 400

    try:
        input = r.recognize_google(audio)

        print("You said: " + input)
        return str(input)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
 
 
 
