#babu_listen_basic.py
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Listening... Speak now")
    recognizer.adjust_for_ambient_noise(source, duration=0.5)
    audio = recognizer.listen(source)

try:
    text = recognizer.recognize_google(audio, language="en-US")
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I could not understand.")
except sr.RequestError as e:
    print("API error:", e)
