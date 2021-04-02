from djitellopy import tello
import speech_recognition as sr 
global me, r
me = tello.Tello()
me.connect()
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over")    
    try:
        print("Text: "+r.recognize_google(audio_text))
    except:
         print("Sorry, I did not get that")
    if r.recognize_google(audio_text) == 'take off':
        me.takeoff()
    if r.recognize_google(audio_text) == 'forward':
        me.move_forward(50)
    if r.recognize_google(audio_text) == 'backward':
        me.move_back(50)
    if r.recognize_google(audio_text) == 'right':
        me.rotate_clockwise(45)
    if r.recognize_google(audio_text) == 'left':
        me.rotate_counter_clockwise(45)
    if r.recognize_google(audio_text) == 'up':
        me.move_up(10)
    if r.recognize_google(audio_text) == 'down':
        me.move_down(10)
    if r.recognize_google(audio_text) == 'land':
        me.land()
