import speech_recognition as sr
import pyttsx3
import ollama
import spacy
from datetime import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

# Load NLP model for intent recognition
nlp = spacy.load("en_core_web_sm")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (Say 'exit' to stop)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"User: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand that."
    except sr.RequestError:
        return "Could not request results, check your internet connection."

def recognize_intent(text):
    doc = nlp(text)
    
    if "weather" in text:
        return "weather"
    elif "time" in text:
        return "time"
    elif "news" in text:
        return "news"
    else:
        return "general_query"

def generate_response(prompt, intent):
    if intent == "weather":
        response = "The current weather is sunny with a temperature of 25°C."
    elif intent == "time":
        response = f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif intent == "news":
        response = "Today's top news: Scientists discover new black hole!"
    else:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
        response = response['message']['content']
    
    return response

def speak_response(response_text):
    print(f"AI: {response_text}")
    engine.say(response_text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        user_input = recognize_speech()
        
        if user_input in ["exit", "quit", "stop"]:
            print("Goodbye!")
            speak_response("Goodbye!")
            break
        
        intent = recognize_intent(user_input)
        response = generate_response(user_input, intent)
        speak_response(response)
