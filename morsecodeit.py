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
    """Converts the text into morse"""
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
    """
    Plays the Morse Code using playsound.
    3 speed options available: 'slow','medium','fast'.By default speed is set to default 
    """
    timing = {
    'slow' : [0.25,1.2,1.5],#delay between (dot&dash), words and spaces respectively
    'medium' : [0.05,0.75,1],
    'fast' : [0,0.15,0.5]
    }

    for code in [i for i in encrypted_message ]:
        if code == '.':
            playsound.playsound('./dot.wav')
            time.sleep(timing[speed][0])
        elif code == '-':
            playsound.playsound('./dash.wav')
            time.sleep(0.25)
        elif code == ' ':
            time.sleep(timing[speed][1])
        elif code == '/':
            time.sleep(timing[speed][2])    
 

message = morse_code_converter('sms')
print(message)
play_sound(message,speed='slow')
