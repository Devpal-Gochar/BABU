import speech_recognition as sr
import pyttsx3


# SPEAK

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 165)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


# LISTEN (FIXED)

recognizer = sr.Recognizer()
mic = sr.Microphone()

# Adjust noise ONLY ONCE
with mic as source:
    print("Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=1)

def listen():
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text.lower()
    except:
        return ""

# MAIN LOOP

speak("Hello. I am Babu. I am ready to talk.")

while True:
    command = listen()

    if not command:
        continue

    if "stop" in command or "exit" in command or "quit" in command:
        speak("Okay. Goodbye.")
        break

    if "babu" in command:
        if "name" in command:
            speak("My name is Babu.")
        elif "how" in command:
            speak("I am fine. Thank you.")
        elif "listen" in command or "there" in command:
            speak("Yes. I am listening.")
        else:
            speak("Yes. Tell me.")
    else:
        speak("Please say Babu to talk to me.")




# Import required libraries
# speech_recognition is used to convert
# spoken voice (microphone input) into text
import speech_recognition as sr



# SPEAK FUNCTION (TEXT MODE - STABLE)

# This function represents Babu's "speaking"
# For Phase 1, we use print() instead of voice
# to keep the system stable on laptops
def speak(text):
    # Print Babu's response on the terminal
    # This acts as a placeholder for voice output
    print("BABU:", text)

# LISTEN SETUP


# Create a Recognizer object
# This object processes audio and converts it to text
recognizer = sr.Recognizer()

# Create a Microphone object
# This tells Python which audio input device to use
mic = sr.Microphone()


# MICROPHONE CALIBRATION


# Calibrate the microphone ONCE
# This helps remove background noise
# and improves speech recognition accuracy
with mic as source:
    print("Calibrating microphone...")
    recognizer.adjust_for_ambient_noise(source, duration=1)


# LISTEN FUNCTION


# This function listens to the microphone
# and returns the recognized text
def listen():
    # Open the microphone and start listening
    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Convert speech to text using Google Speech API
        text = recognizer.recognize_google(audio, language="en-US")

        # Print what the user said (for debugging & learning)
        print("You said:", text)

        # Convert text to lowercase for easier comparison
        return text.lower()

    except:
        # If speech is not understood or any error occurs
        # return an empty string instead of crashing
        return ""



# MAIN PROGRAM LOOP


# Initial greeting from Babu when program starts
speak("Hello. I am Babu. I am ready.")

# Infinite loop so Babu keeps listening continuously
while True:

    # Listen to the user's voice input
    command = listen()

    # If nothing was recognized, skip this loop
    if not command:
        continue

   
    # EXIT COMMANDS
   
    # If user says stop / exit / quit
    # Babu says goodbye and exits the program
    if "stop" in command or "exit" in command or "quit" in command:
        speak("Okay. Goodbye.")
        break


   
    # WAKE WORD LOGIC
    
    # Check if the wake word "babu" is present
    if "babu" in command:

        # If user asks Babu's name
        if "name" in command:
            speak("My name is Babu.")

        # If user asks how Babu is
        elif "how" in command:
            speak("I am fine. Thank you.")

        # If user checks whether Babu is listening
        elif "listen" in command or "there" in command:
            speak("Yes. I am listening.")

        # Any other sentence with "babu"
        else:
            speak("Yes. How can I help you?")

    # NO WAKE WORD

    # If the user speaks without saying "babu"
    # Babu politely asks to use the wake word
    else:
        speak("Please say Babu to talk to me.")
