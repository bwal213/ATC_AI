
import speech_recognition as sr

#frequency_sampling, audio_signal = wavfile.read("./Audio_files/Alpha.wav")

r = sr.Recognizer()

file_ = "/Audio_files/Alpha.wav"
path = os.getcwd()+file_

sound = sr.AudioFile(path)
with sound as source:
    audio = r.record(source)

print(r.recognize_google(audio))

#with sr.Microphone() as source: recording.adjust_for_ambient_noise(source)
#print("Say Something:")
#audio = recording.listen(source)
