import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from a microphone (you can also load an audio file)
with sr.Microphone() as source:
    print("Please speak something...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds

# Recognize the speech using Google Web Speech API
try:
    text = recognizer.recognize_google(audio)
    print("You said:", text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand your speech.")
except sr.RequestError as e:
    print(f"Error connecting to the Google Web Speech API: {e}")

# Optionally, you can save the recognized text to a file
with open("recognized_text.txt", "w") as file:
    file.write(text)
