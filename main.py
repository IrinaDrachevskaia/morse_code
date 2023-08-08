dictionary = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M':	'--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R':	'.-.', 'S':	'...', 'T':	'-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z':	'--..',
              '0': '-----', '1': '.----',	'2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
              ' ': '/',
              '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
              '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=':	'-...-', '+': '.-.-.',
              '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.', '¿': '..-.-', '¡': '--...-'
}

def encrypt(text, morse_text):
    text = text.upper()
    letters = list(text)
    for symbol in text:
        morse_text += dictionary[symbol]
        morse_text += ' '
    print(f'Your morse code: {morse_text}')

def decrypt(text, morse_text):
    morse_text = morse_text.split()
    for symbol in morse_text:
        for k, v in dictionary.items():
            if v == symbol:
                text+=k
    print(f'Your decrypted text: {text}')

def check_finish(finish):
    if finish.lower() == 'y':
        return True

    else:
        return False


go_on = True
print('Welcome to Morse Code Translator')
while go_on:
    answer = input('If you want to encrypt the text to morse code type - Y. If you want to decrypt the morse code, type - N: ')
    if answer.upper() == 'Y':
        text = input('Type your text: ')
        morse_text = ''
        encrypt(text, morse_text)
        finish = input('Would you like try again? Type Y or N: ')
        go_on = check_finish(finish)

    elif answer.upper() == 'N':
        morse_text = input('Type your morse code: ')
        text = ''
        decrypt(text, morse_text)
        finish = input('Would you like try again? Type Y or N: ')
        go_on = check_finish(finish)
    else:
        print('You typed wrong answer, try again')






