import playsound
import time

MORSE_CODE_DICT = { 
'A':'.-', 'B':'-...', 
'C':'-.-.', 'D':'-..', 'E':'.', 
'F':'..-.', 'G':'--.', 'H':'....', 
'I':'..', 'J':'.---', 'K':'-.-', 
'L':'.-..', 'M':'--', 'N':'-.', 
'O':'---', 'P':'.--.', 'Q':'--.-', 
'R':'.-.', 'S':'...', 'T':'-', 
'U':'..-', 'V':'...-', 'W':'.--', 
'X':'-..-', 'Y':'-.--', 'Z':'--..', 
'1':'.----', '2':'..---', '3':'...--', 
'4':'....-', '5':'.....', '6':'-....', 
'7':'--...', '8':'---..', '9':'----.', 
'0':'-----', ', ':'--..--', '.':'.-.-.-', 
'?':'..--..', '/':'-..-.', '-':'-....-', 
'(':'-.--.', ')':'-.--.-'
} 


def morse_code_converter(message):
    encrypted_message = ''
    for letter in [i.upper() for i in message]:
        if letter in MORSE_CODE_DICT:
            for character in MORSE_CODE_DICT:
                if letter == character:
                    encrypted_message += MORSE_CODE_DICT[character]+' '
        elif letter == ' ':
            encrypted_message += '/ '
    return encrypted_message
    

def play_sound(encrypted_message,speed='medium'):
    timing = {
    'slow' : [1.2,1.5],
    'medium' : [0.75,1],
    'fast' : [0.15,0.5]
    }

    for code in [i for i in encrypted_message ]:
        if code == '.':
            playsound.playsound('./dot.wav')
        elif code == '-':
            playsound.playsound('./dash.wav')
        elif code == ' ':
            time.sleep(timing[speed][0])
        elif code == '/':
            time.sleep(timing[speed][1])    


message = morse_code_converter('Hello my name is akshaj dev and I created this program')
print(message)
play_sound(message)
