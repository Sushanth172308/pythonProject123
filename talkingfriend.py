import pyttsx3

vtf = pyttsx3.init()

""" RATE"""
rate = vtf.getProperty('rate')   # getting details of current speaking rate                      #printing current voice rate
vtf.setProperty('rate', 130)     # setting up new voice rate

def vtf_speak(text):
    print('speaking...')
    vtf.say(text)
    vtf.runAndWait()


txt = 'Hello buddies, how are you all doing!'
vtf_speak(txt)

while txt !='bye':
    txt = input('what should i say:')
    txt = txt.lower()
    vtf_speak(txt)
    if txt !='bye':
        vtf_speak(txt)
else:
    vtf_speak('see you again, nice talking with you')
