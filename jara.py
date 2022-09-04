#import libraries
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sys

def screen_clear():
    if os.name == 'posix': 
        os.system('clear')

    else:
        os.system("cls")    

screen_clear()        

#set up speech engine
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<=12:
        print("good morning sir...")
        speak("good morning sir...")
    elif hour>=12 and hour<18:
        print("good afternoon sir..")
        speak("good afternoon sir..")
    else:
        print("good evevning sir...")    
        speak("good evevning sir...") 
wishMe()

def bye():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
            print('Bye Bye, Have a Good Day.')
            speak("Bye Bye, Have a Good Day.")
        
    elif hour>=12 and hour<18:
            print('Bye Bye, Enjoy Your Evening.')
            speak("Bye Bye, Enjoy Your Evening.")
        
    else:
            print('Bye Bye, Good Night')
            speak("Bye Bye, Good Night")  
    
print('i am jara  , please tell me how may I help you..')
speak('i am jara , please tell me how may I help you..')

#function to recognize spoken command and convert to text
def takecommand():
    
    r = sr.Recognizer()     
    with sr.Microphone() as source:  
        print('listening.....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio,language='en,in')   
        print(f"user said:{query}\n") 

    except Exception as e: 
      print("say that again please...")
      return "none"

    return query


if __name__ == "__main__":
 while True:  #you can use the above query to perform tasks as per requirements.
     query = takecommand().lower()
     if 'wikipedia' in query:
        speak("searching wikipedia.....")
        query = query.replace('wikipedia', "")
        results = wikipedia.summary(query,sentences=2)
        speak("according to wikipedia")
        print(results)
        speak(results)

     elif 'open youtube'in query:
        webbrowser.open("youtube.com")  
     elif 'open google'in query:
        webbrowser.open("google.com")  

     elif 'Sidhu Mooose Wala'in query:
        webbrowser.open("https://www.youtube.com/watch?v=twCHVhk8iMU&list=RDEMgI0yUYIcvlfsHsDpesMRnw&start_radio=1")

     elif 'punjabi songs'in query:
        webbrowser.open("https://www.youtube.com/watch?v=6xoB4ZiKKn0&list=PL-oM5qTjmK2vxdTsj2Xghu5fjxhtuMaxo")  

     elif 'who made you' in query:
            print('Mr. Sohail Made me on 3 september of 2022.')
            speak("Mr. sohail Made me on 3 september of two thousand twenty-two")
     
     elif 'who are you' in query:
            print('I am jara. A AI Assitant my coding written in Python Progamming By Mr. Sohail on 3 september of 2022.')       
            speak("I am jaara. A AI Assitant my coding written in Python Progamming By Mr. Sohail on 3 september of two thousand twenty-two")

     elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"Sir, the time is {strTime}")   
            speak(f"Sir, the time is {strTime}")     

     elif 'chrome' in query:
            chromePath = "path" #Give path to file
            os.startfile('"C:\Program Files\Google\Chrome\Application\chrome.exe"')

     elif 'how are you' in query:    
            print("I'm Fine Sir, How about you.")
            speak("I'm Fine Sir, How about you")
     elif 'Im Good' in query:    
            print("That is very good.")
            speak("That is very good")

     elif 'exit' in query:
            bye()
            sys.exit()

