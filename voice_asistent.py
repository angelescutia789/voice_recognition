#pip install pipwin
#pipwin install speechrecognition
#pip install --upgrade speechrecognition
import webbrowser
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print('Helllo, i´m your personal asistent: ')
    audio= r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('You Said:{}'.format(text))
        print (text)
        if "amazon" in text:
            webbrowser.open('http://amazon.com.mx')
             if "facebook" in text:
            webbrowser.open('http://facebook.com.mx')
             if "twitter" in text:
            webbrowser.open('http://twitter.com.mx')
             if "google" in text:
            webbrowser.open('http://google.com.mx')
             if "notices" in text:
            webbrowser.open('http://news.com.mx')
            except:
                print('I can´t understand you')

