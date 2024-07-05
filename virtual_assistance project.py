import pyttsx3
import speech_recognition as sr
import pyjokes
import pywhatkit
from webscout import Phindv2
import datetime
import pywhatkit as kit
from tmdbv3api import TMDb, Movie


def speak(text): 
  engine=pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        text=r.recognize_google(audio)
        return text
    
def operation(text):
    if "joke" in text:
        joke=pyjokes.get_joke()
        print(joke)
        speak(joke)
        
    elif"search" in text:
        ph=Phindv2()
        response=ph.ask(text)
        message = ph.get_message(response)
        print(message)
        speak(message)
        
        
    elif "youtube" in text.lower():
        pywhatkit.playonyt(text)
        print("playing...")
      
      
    elif"time"in text:
      current_datetime = datetime.datetime.now()
      print(current_datetime)
      speak(f"Current Date and Time is {current_datetime}")


    elif"send message"in text:
        
        phone_number = "+91 8194986789"
        message = "Hello! how are you"
        kit.send_message(phone_number, message, 11, 44)
        
    elif "movie" in text:
      tmdb = TMDb()
      tmdb.api_key ="0fa2fb1a7b7c3804310a891034105866"
      tmdb.language = 'en'
      tmdb.debug = True
      movie = Movie()
      popular = movie.popular()

      for p in popular:
          speak(p.title)
          print(p.title)
      
      
if __name__=="__main__":
    try:
      speak("hello chaaru,how may i assist you today?")
      print('say something')
      text=listen()
      print(text)
      operation(text)
    
    except Exception as e:
        print("error! say something again")
        
        




