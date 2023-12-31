import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alpha' in command:
                command = command.replace('alpha', '')
                print(command)
    except:
        command = ""  # Initialize command with an empty string if an exception occurs
    return command



def run_alpha():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('am not single.')
    elif 'i love you' in command:
        talk('I love you too')
    elif 'hello' in command:
        talk('I am fine. How are you doing? I hope your day goes well Dennis.')
    elif 'who are you' in command:
        talk('My name is Alpha. I am a simple artificial intelligence program developed by Dennis.')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'hey you' in command:
        talk('hey you too')
    elif 'search for ' in command:
        query = command.replace('search for ', '')
        talk('Searching for s' + query + ' on Google')
        pywhatkit.search(query)
    else:
        talk('Am sorry i did not understand what you said.  Remember I cannot access local variable command where it is not associated with a value. Please say the command again, also ensure that the command is in the search parameters restricted by Dennis')


while True:
    run_alpha()
