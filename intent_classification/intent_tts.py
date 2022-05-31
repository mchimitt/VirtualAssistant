import pyttsx3
import speech_recognition as sr


# function that takes in user's words
def listen():
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
            return "null"
    # return a string of data (in lowercase) that was detected from the user's voice
    return data.lower()


def say(text):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    print(rate)
    engine.setProperty('rate', 115)

    # TODO: FIGURE OUT IF THE DELAY ON THE AUDIO IS BECAUSE OF MY HEADPHONES POTENTIAL FIX: APPEND EMPTY
    #  CHARACTERS LIKE EITHER A PERIOD OR SOME SPACES TO MAKE THE AUDIO LONGER IN THE BEGINNING

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
