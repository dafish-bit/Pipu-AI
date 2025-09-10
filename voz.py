import speech_recognition as speech_recog
#### V1 - función
def speech():
    try:
        mic = speech_recog.Microphone()
        recog = speech_recog.Recognizer()
        with mic as audio_file:
            print("Habla ):<")
            recog.adjust_for_ambient_noise(audio_file)
            audio = recog.listen(audio_file)
            return recog.recognize_google(audio, language="es-GB")
    except Exception as e:
        return f"Ni idea ¯\_(ツ)_/¯ {e}"
print(speech())