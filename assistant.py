import speech_recognition as sr
import pyttsx3
from intent_classification.intent_classifier import IntentClassifier
from intent_functions.weather import determine_weather


# Assistant Class
class Assistant:

    # Constructor
    def __init__(self, name, rate):
        self.rate = rate
        self.name = name
        self.classifier = IntentClassifier()

    def greet(self):
        greeting = f"Hello, my name is {self.name}. I am your personal assistant."
        self.say(greeting)

    # function that takes in user's words
    def listen(self):
        # getting the speech recognizer r
        r = sr.Recognizer()
        # getting microphone data
        with sr.Microphone() as source:
            audio = r.listen(source)
            data = ""
            # performing a try, where we attempt to get user voice data
            try:
                data = r.recognize_google(audio)
                print(data)
            # print exception if one occurs
            except Exception as e:
                print("Exception: " + str(e))
        # return a string of data (in lowercase) that was detected from the user's voice
        return data.lower()

    def say(self, text):
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        print(rate)
        engine.setProperty('rate', self.rate)

        # TODO: FIGURE OUT IF THE DELAY ON THE AUDIO IS BECAUSE OF MY HEADPHONES POTENTIAL FIX: APPEND EMPTY
        #  CHARACTERS LIKE EITHER A PERIOD OR SOME SPACES TO MAKE THE AUDIO LONGER IN THE BEGINNING

        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    # Start function for the assistant; Runs the infinite loop
    def start(self):
        while True:
            # getting the user input from the users voice
            print("looping")
            text = self.listen()

            # if the name of the assistant is in the stream of text, then the wake word is said
            if text.count(self.name) > 0:
                self.say("What would you like?")
                print("listening")
                # get new stream of input from user (get command)
                text = self.listen()
                # classify the intent of the user input
                classification = self.classifier.predict(text)
                print(classification)

                # Do an action depending on the intent
                if classification == 'weather':
                    determine_weather()
                if classification == 'greeting':
                    self.greet()
