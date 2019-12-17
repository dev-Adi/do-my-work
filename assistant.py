import pyttsx3 # to install type in terminal pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia
import webbrowser
import os
import wolframalpha
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[1].id)
rate = engine.setProperty('rate',175)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("good evening")
    
    speak("I am your assistant, how may i help you")

def takeCommand():
    #it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("recognising..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please ...")
        return "none"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('svvvcsc1@gmail.com','padhlothoda')
    server.sendmail('svvvcsc1@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            #c = webbrowser.get('chrome')
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'D:\\music a\\New Folder'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = ""
            os.startfile(codePath)

        elif 'email to aditya' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "svvvcsc1@gmail.com"
                sendEmail(to,content)
                speak("email sent")
            except Exception as e:
                print(e)
                speak("mail not sent")

        elif 'calculate' in query:
            app_id= "Y5992T-VRLEYGLKKH"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            speak("The answer is " + answer)

        elif 'weather' in query:
            app_id= "Y5992T-VRLEYGLKKH"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'convert' in query:
            app_id= "Y5992T-VRLEYGLKKH"
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            speak("The answer is " + answer)

        elif 'search' in query:
            query = query.replace("search","")
            webbrowser.open(query)

        elif 'exit' in query or 'quit' in query or 'shutdown' in query:
            speak("thankyou see you soon")