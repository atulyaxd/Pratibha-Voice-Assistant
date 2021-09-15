import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import time
import wolframalpha
import requests

engine = pyttsx3.init()
engine.setProperty("rate",178)#speed of speech
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def takeCommand():
    r=sr.Recognizer()
    my_mic_device = sr.Microphone()
    with my_mic_device as source:
            #speak("Listening")
            audio = r.listen(source)

    try:
        speak("recognising")
        query = r.recognize_google(audio)
        print(query)
    
    except Exception as e:
        speak("Unable to get you, kindly repeat your words ...")
        return "None"

    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

        
def greet():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
            speak("hello Good Morning")
    elif hour>=12 and hour<18:
            speak("hello Good Afternoon")
    else:
            speak("hello Good Evening")


if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()

        if "calculate" in query:
             
            app_id = "8U4UJA-GG7RAH45KU"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
       
        elif "how are you" in query:
            speak("I'm fine, how about you")

        elif " " in query:
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)

        elif "what is" in query or "who is" in query:
             
            # Use the same API key
            # that we have generated earlier
            client = wolframalpha.Client("8U4UJA-GG7RAH45KU")
            res = client.query(query)
             
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print("no results")
                query = takeCommand().lower()     

        elif "study" in query:
                def pomodoror():
                    speak("Pomodoro starts now! focus for 25 minutes play for 5 minutes")
                    for i in range(4):
                        t = 25*60
                        while t: 
                            mins = t // 60 
                            secs = t % 60
                            timer = '{:02d}:{:02d}'.format(mins, secs) 
                            print(timer, end="\r") # overwrite previous line 
                            time.sleep(1)
                            t -= 1 
                        speak("Break Time!!")

                        t = 5*60 
                        while t: 
                            mins = t // 60 
                            secs = t % 60
                            timer = '{:02d}:{:02d}'.format(mins, secs) 
                            print(timer, end="\r") # overwrite previous line 
                            time.sleep(1)
                            t -= 1 
                        speak("Work Time!!")
                pomodoror()           

        """if "Pratibha" in query:
            speak("Pratibha (Hindi : प्रतिभा) is a Hindu Sanskrit Indian feminine given name, which means genius.")
            speak("As “Pratibha” the name suggests, i am going to be your learning fellow, i am a web-browser based voice assistant that works on python3.")
            speak("I retrieve the required informations through the requests sent through APIs and the data received in the text format,  I convert it into speech. ")
            speak("I am capable of giving information for any specific proper nouns. For example, poet Rabindranath Tagore, monument Taj Mahal etc.")"""
        
        if "exit" in query:
            speak("Bye")
            exit()            