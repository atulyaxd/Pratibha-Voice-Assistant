"""
Project : Pratibha-Voice-Assistant
Author : Atulya Bharat @itsatulya
Version : 1.0
"""
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import time
import wolframalpha

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
        print(f"User: {query}")
    
    except Exception as e:
        print("Pratibha: Unable to get you, kindly repeat your words ...")
        speak("Unable to get you, kindly repeat your words ...")
        return "None"

    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

        
def greet():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
            print("Pratibha: Hello! Good Morning")
            speak("hello Good Morning")
    elif hour>=12 and hour<18:
            print("Pratibha: Hello! Good Afternoon")
            speak("hello Good Afternoon")
    else:
            print("Pratibha: Hello! Good Evening")
            speak("hello Good Evening")


if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()

        if "calculate" in query:
             
            app_id = "your_apiid"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print(f"Pratibha: The answer is {answer}")
            speak("The answer is " + answer)
       
        elif "how are you" in query:
            print("Pratibha: I'm fine, how about you?")
            speak("I'm fine, how about you")

        elif " " in query:
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=3)
            print(f"Pratibha: {results}")
            speak("According to Wikipedia")
            speak(results)

        elif "what is" in query or "who is" in query:
             
            client = wolframalpha.Client(app_id)
            res = client.query(query)
             
            try:
                result = next(res.results).text
                print(f"Pratibha: {results}")
                speak (next(res.results).text)
            except StopIteration:
                print("Pratibha: no results")
                query = takeCommand().lower()     

        elif "study" in query:
                def pomodoror():
                    speak("Pomodoro starts now! focus for 25 minutes play for 5 minutes")
                    for i in range(4):
                        t = 25*60
                        while t: 
                            mins = t // 60 
                            secs = t % 60
                            timer = 'Time Left: {:02d}:{:02d}'.format(mins, secs) 
                            print(timer, end="\r") # overwrite previous line 
                            time.sleep(1)
                            t -= 1 
                        print("Pratibha: Break Time!!")
                        speak("Break Time!!")

                        t = 5*60 
                        while t: 
                            mins = t // 60 
                            secs = t % 60
                            timer = 'Time Left: {:02d}:{:02d}'.format(mins, secs) 
                            print(timer, end="\r") # overwrite previous line 
                            time.sleep(1)
                            t -= 1 
                        print("Pratibha: Back to work!!")
                        speak("Back to work!!")
                pomodoror()           
                
        if "exit" in query:
            speak("Bye")
            exit()          
