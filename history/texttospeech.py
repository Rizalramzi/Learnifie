import pyttsx3
text_speech = pyttsx3.init()
answer = input("Lets Type something : ")
text_speech.say(answer)
text_speech.runAndWait()