
import webbrowser
import string
import speech_recognition as sr

# obtain audio 
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Hello, what can i help you find?[Player lookup,Weather,resturants, or just to search the web: ]")
    audio = r.listen(source)
    
    
    

if "player" in r.recognize_google(audio):
    # obtain audio from the microphone
    r2 = sr.Recognizer()
    url = 'https://en.wikipedia.org/wiki/'
    with sr.Microphone() as source:
        print("Say any sports players name to see there Bio: ")
        audio2 = r2.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r2.recognize_google(audio2))
            webbrowser.open_new(url+r2.recognize_google(audio2))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))


if "weather" in r.recognize_google(audio):
    # obtain audio from the microphone
    r3 = sr.Recognizer()
    url3 = 'https://www.wunderground.com/us/'
    with sr.Microphone() as source:
        print("Please say a city and state: ")
        audio3 = r3.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r3.recognize_google(audio3))
            webbrowser.open_new(url3+r3.recognize_google(audio3))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))


if "restaurants" in r.recognize_google(audio):
    # obtain audio from the microphone
    r4 = sr.Recognizer()
    url4 = 'https://www.yelp.com/search?cflt=restaurants&find_loc='
    with sr.Microphone() as source:
        print("Please state a location to search for restaurants: ")
        audio4 = r4.listen(source)

        try:
            print("Google Speech Recognition thinks you said " + r4.recognize_google(audio4))
            webbrowser.open_new(url4+r4.recognize_google(audio4))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e))

if "search" in r.recognize_google(audio):
    # obtain audio from the microphone
    r5 = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("what website would you like me to search for you? ")
        audio5 = r5.listen(source)
        url5= r5.recognize_google(audio5)

        try:
            print("Google Speech Recognition thinks you said " + r5.recognize_google(audio5))
            webbrowser.open_new("https://"+url5+".com")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
               print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
