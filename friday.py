import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening  Sir!")

    speak("I am Friday. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-Us')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('hmehedi953@gmail.com', 'm21324611')
    server.sendmail('mehedi.mbstu.ict.13@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'hay' in query:
            speak('Yes Sir, I am here for you...')

        elif 'who are you' in query:
            speak('I am Friday! Iron Man updated creation. version 2.0')


        elif 'hi' in query:
            speak('Hi Sir...')

        elif 'nothing' in query:
            speak('okay Sir...')

        elif 'how can you help' in query:
            speak('I can help you what i have programed Sir!...')

        elif 'what is python' in query:
            speak('Python is an interpreted, object-oriented, high-level programming language ...')

        elif 'i love you friday' in query:
            speak('I Love You Too Sir! Thank you...')

        elif 'hello friday' in query:
            speak('Welcome Home Sir!, I am here for you...')

        elif 'boyfriend' in query:
            speak('no Sir!I have no boyfriend Sir! I am here for you...')

        elif 'who create you' in query:
            speak('Mehedi hasan created me...')

        elif 'created you' in query:
            speak('Mehedi hasan created me...')

        elif 'your boss' in query:
            speak('Mehedi hasan...')

        elif 'thank you' in query:
            speak('You are welcome Sir..')

        elif 'iron man' in query:
            speak(' Iron man is the one who created me.')
            speak('He is a legend! I Love Him too!...')


        elif 'exit' in query:
            speak('Okay Sir, I am going to sleep now!...')
            speak('I Love you 3000!...')

        elif 'beautiful' in query:
            speak('Thank you so much Sir!...')

        elif 'can you sing' in query:
            speak('Thank you  Sir! but I can not sing...')
            speak('But I can help you for your song from youtube.can I?..')

        elif 'ok play' in query:
            speak('Okay playing Sir!...')
            webbrowser.open("https://www.youtube.com/watch?v=hHNJSMUgWBM")


        elif 'sweet' in query:
            speak('Thank you Sir!...')

        elif 'how are you' in query:
            speak('I am absulately fine Sir....')
            speak('How are you Sir?....')






        elif 'open youtube' in query:
            speak('Ok Sir, I am opening youtube...')
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak('Ok Sir, I am opening google...')
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak('Ok Sir, I am opening stackoverflow...')
            webbrowser.open("stackoverflow.com")

        elif 'google map' in query:
            speak('Sure Sir! which place do you want to search?')

        elif 'dhaka' in query:
            speak('Ok Sir, I am working on it...')
            webbrowser.open("https://www.google.com/maps/place/Dhaka/@23.7808875,90.2792371,43668m/data=!3m2!1e3!4b1!4m5!3m4!1s0x3755b8b087026b81:0x8fa563bbdd5904c2!8m2!3d23.810332!4d90.4125181")
            speak('Here it is! ')




        elif 'play music' in query:
            speak('Ok Sir, I am playing music for you...')
            music_dir = 'E:\\Alan'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\MEHEDI\\Desktop\\Jervis"
            os.startfile(codePath)

        elif 'mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "mehedi.mbstu.ict.13@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry  Sir. I am not able to send this email")
