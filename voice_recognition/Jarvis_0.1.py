import speech_recognition as sr
from playsound import playsound
from voice_recognition.web_searcher.web_searcher import Web
import pyttsx3


# Recognizer init
r = sr.Recognizer()

# Text to speech init
engine = pyttsx3.init()

# Voice setup
# 0 = female
# 1 = male
voices = engine.getProperty('voices')
# engine.setProperty("voice", voices[0].id)
engine.setProperty("voice", voices[1].id)

# How fast the machine will speak
engine.setProperty('rate', 170)


""" 
Listening for commands
@:param ask - the question machine should ask
@:return voice_data - what the user said
"""
def listen(ask = ''):
    # Turning the mic on
    with sr.Microphone() as source:
        speak(ask)
        audio = r.listen(source, phrase_time_limit=5)
        print("Done listening.")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        # Did not understand
        except sr.UnknownValueError:
            speak("Apologies, but I did not understand.")
        # Service is not working
        except sr.RequestError:
            speak("Apologies, but the service is down.")
    print(voice_data.lower())
    return voice_data.lower()


def lookForWord(words):
    for word in words:
        if word in voice_data:
            return True

""""
Takes what the user said and respond with a proper answer calling the method speak
@:param response - what the user said
"""
def respond(response):
    # greeting
    if lookForWord(["hey", "hi", "hello"]):
        speak("Greetings Sir")
        return
    
    # saying name
    if lookForWord(["what is your name", "what's your name", "tell me your name"]):
        speak("I am Jarvis. Your personal assistant sir.")
        return
    
    # searching on Google
    if lookForWord(["search", "look for", "google"]) and "youtube" not in voice_data and "images" not in voice_data:
        search_term = voice_data.split("for")[-1]
        web = Web()
        web.searchForPhrase(search_term)
        speak("Here is what I found about " + search_term)

    # searching on YouTube
    if lookForWord(["youtube"]):
        search_term = voice_data.split("for")[-1]
        web = Web()
        web.searchYoutube(search_term)
        speak("Here is what I found on youtube about" + search_term)

    # searching on Google images
    if lookForWord(["images", "image", "pictures", "picture"]):
        search_term = voice_data.split("for")[-1]
        web = Web()
        web.showImages(search_term)
        speak("Here are some images for " + search_term)

    # exits
    if lookForWord(["exit", "quit", "die", "sleep"]):
        return False

    # play music
    if lookForWord(["music", "song", "songs"]) and "youtube" not in voice_data:
        playsound("dep/audio/hooked.wav")

    # introduce
    if lookForWord(["intro", "introduce", "who are you"]):
        playsound("dep/audio/jarvis_init.mp3")


"""
Says what is passed as an argument using machine's mic
@:param to_be_spoken - what the machine should say
"""
def speak(to_be_spoken):
    say = str(to_be_spoken)
    print(say)
    engine.say(say)
    engine.runAndWait()



playsound("dep/audio/jarvis_intro.wav")
# Main loop
while True:
    voice_data = listen("Recording")
    if False == respond(voice_data):
        break
