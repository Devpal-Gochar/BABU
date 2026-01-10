import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 165)
engine.setProperty('volume', 1)
# engine.runAndWait()
engine.say("Hello, I am Babu")
engine.say("नमस्ते, मैं बाबू हूँ",)
engine.runAndWait()

