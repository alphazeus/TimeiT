
import winsound

def soundCheck():
    print("Checking sound...")
    winsound.Beep(1000, 500)

def playShortBeep():
    winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)