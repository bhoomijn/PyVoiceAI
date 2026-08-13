
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import urllib.parse
import os


# -----------------------------
# Text-to-Speech Setup
# -----------------------------
engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


# -----------------------------
# Voice Input
# -----------------------------
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=0.5
        )

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:
            speak("I did not hear anything. Please try again.")
            return ""

    try:
        command = recognizer.recognize_google(audio)

        print("You:", command)

        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I could not understand you. Please repeat.")
        return ""

    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""


# -----------------------------
# Open Website
# -----------------------------
def open_website(url, message):
    speak(message)
    webbrowser.open(url)


# -----------------------------
# Command Handler
# -----------------------------
def handle_command(command):

    # Greeting
    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")

    # Date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {current_date}.")

    # Day
    elif "day" in command:
        current_day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {current_day}.")

    # YouTube
    elif "youtube" in command:
        open_website(
            "https://www.youtube.com",
            "Opening YouTube."
        )

    # Google
    elif "google" in command:
        open_website(
            "https://www.google.com",
            "Opening Google."
        )

    # Search
    elif command.startswith("search"):

        query = command.replace(
            "search",
            "",
            1
        ).strip()

        if query:
            encoded_query = urllib.parse.quote_plus(query)

            url = (
                "https://www.google.com/search?q="
                + encoded_query
            )

            speak(f"Searching for {query}.")
            webbrowser.open(url)

        else:
            speak("Please tell me what you want to search for.")

    # Play something on YouTube
    elif command.startswith("play"):

        query = command.replace(
            "play",
            "",
            1
        ).strip()

        if query:
            encoded_query = urllib.parse.quote_plus(query)

            url = (
                "https://www.youtube.com/results?search_query="
                + encoded_query
            )

            speak(f"Searching YouTube for {query}.")
            webbrowser.open(url)

        else:
            speak("Please tell me what you want to play.")

    # Open GitHub
    elif "github" in command:
        open_website(
            "https://github.com",
            "Opening GitHub."
        )

    # Open LinkedIn
    elif "linkedin" in command:
        open_website(
            "https://www.linkedin.com",
            "Opening LinkedIn."
        )

    # Open Gmail
    elif "gmail" in command:
        open_website(
            "https://mail.google.com",
            "Opening Gmail."
        )

    # Current working directory
    elif "where am i" in command or "current folder" in command:
        folder = os.getcwd()
        speak(f"You are currently working in {folder}.")

    # Exit
    elif (
        "exit" in command
        or "quit" in command
        or "stop" in command
        or "goodbye" in command
    ):
        speak("Goodbye! Have a great day.")
        return False

    # Unknown command
    else:
        speak(
            "I don't know that command yet. "
            "Please try another command."
        )

    return True


# -----------------------------
# Main Program
# -----------------------------
def main():

    speak(
        "Voice assistant started. "
        "How can I help you?"
    )

    running = True

    while running:

        command = listen()

        if command:
            running = handle_command(command)


# -----------------------------
# Program Entry Point
# -----------------------------
if __name__ == "__main__":
    main()
