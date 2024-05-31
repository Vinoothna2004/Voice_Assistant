import speech_recognition as sr
import pyttsx3
import datetime
import requests
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand it.")
            return ""
        except sr.RequestError:
            speak("Apologize, my speech service is down.")
            return ""

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%H:%M")

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def search_web(query):
    # Implement a basic web search
    speak(f"Searching the web for {query}")
    # This is a placeholder, actual implementation may vary
    url = f"https://www.google.com/search?q={query}"
    return url

def main():
    speak("Hello, how can I help you today?")
    while True:
        command = recognize_speech()
        if 'hello' in command:
            speak("Hi there!")
        elif 'time' in command:
            speak(f"The current time is {get_time()}")
        elif 'date' in command:
            speak(f"Today's date is {get_date()}")
        elif 'search' in command:
            query = command.replace("search", "").strip()
            url = search_web(query)
            speak(f"Here is what I found: {url}")
        elif 'exit' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()




