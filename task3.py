import speech_recognition as sr
import pyttsx3

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I did not hear your request. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def process_command(command):
    if "hello" in command:
        speak("Hello! How can I help you today?")
    elif "goodbye" in command:
        speak("Goodbye! Have a great day!")
        exit()
    else:
        speak("I'm sorry, I didn't understand that command.")

if __name__ == "__main__":
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        user_input = listen()
        if user_input:
            process_command(user_input)
