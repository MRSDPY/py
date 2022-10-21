import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source, timeout=1)
    # try:
    data = r.recognize_google(audio, language="eng-in")
    print(data)
    # except sr.UnknownValueError:
    #     print("Error Occur")
