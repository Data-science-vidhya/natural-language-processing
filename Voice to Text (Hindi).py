import speech_recognition as sr
from googletrans import Translator

r= sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something in Hindi")
    audio=r.listen(source)
    print("Time Over, Thanks.")

try:
    print("You Said: "+r.recognize_google(audio))
    print("You Said: "+ r.recognize_google(audio, language= 'hi-IN'))

except:
    pass;
