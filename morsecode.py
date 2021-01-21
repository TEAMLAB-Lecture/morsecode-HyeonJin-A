# -*- coding: utf8 -*-
import re

# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code


# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()

    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message


def is_help_command(user_input):
    if (user_input.lower() =="help" or user_input.lower() == 'h'):
        return True
    else : return False

def is_validated_english_sentence(user_input):
    if(len(re.sub('[^ a-zA-Z!?,.]','',user_input))<len(user_input)): return False
    else: return True
    
def is_validated_morse_code(user_input):
    morse_code_dict = get_morse_code_dict()
    if (len(re.sub('[^ .-]','',user_input))<len(user_input)): return False
    input_list = user_input.split()
    if (len([s for s in input_list if(s in morse_code_dict.values())])<len(input_list)): return False
    return True

def get_cleaned_english_sentence(raw_english_sentence):
    result = re.sub('[.,!?]','',raw_english_sentence)
    return re.sub(' +',' ',result).strip()

def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    inv_morse_dict = {v: k for k,v in morse_code_dict.items()}
    return inv_morse_dict[morse_character]

def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character]

def decoding_sentence(morse_sentence):
    return ''.join([' ' if(s=='') else decoding_character(s) for s in morse_sentence.split(' ')]).strip()

def encoding_sentence(english_sentence):
    clean_sentence = get_cleaned_english_sentence(english_sentence.upper())
    return ' '.join(['' if(s==' ') else encoding_character(s) for s in clean_sentence])




def main():
    print("Morse Code Program!!")
    while True:
        user_input = input("Input your message(H - Help, 0 - Exit):")
        if(user_input=='0'): break
        if(is_help_command(user_input)): print(get_help_message())
        elif(is_validated_morse_code(user_input)): print(decoding_sentence(user_input))
        elif(is_validated_english_sentence(user_input)): print(encoding_sentence(user_input))
        else: print("Wrong Input")
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()
