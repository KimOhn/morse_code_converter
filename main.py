MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
                    '(':'-.--.', ')':'-.--.-'}
#encrypt an english word using the morse code
def encrypt(phrase):
    encoded = ""
    phrase = phrase.upper()
    for i in phrase:
        if i != " ":
            encoded += MORSE_CODE_DICT[i] + " "
        else:
            encoded += "  "
    encoded += " "
    return encoded

#create an aid function to the decrypt function to enable parsing by each item in the list
def lookup(coded_word):
    for i in MORSE_CODE_DICT:
        if MORSE_CODE_DICT[i] == coded_word:
            result = i
    return result

#split by a space to detect each character then run the lookup function for each character
def decrypt(phrase):
    character_lst = phrase.split(" ")
    decoded = ''
    for char in character_lst:
        if char != '':
            decoded +=  lookup(char)
        else:
            decoded += ' '
    return decoded


def main():
    #switch between encrypt or decrypt functions based on the user choice
    operations = {
        "e": encrypt,
        "d": decrypt
    }
    encrypt_or_decrypt = input("would you like to encrypt to a morse code or decrypt a morse code? enter (e/d)")
    #give feedback to the users on their chosen option to encrypt/decrypt
    if encrypt_or_decrypt == 'e':
        user_op = 'encrypt'
    elif encrypt_or_decrypt == 'd':
        user_op = 'decrypt'
    else:
        user_op = 'invalid'
    print(f'ok. your input was {user_op}')
    #if user input was valid, run either the encrypt or the decrypt function based on the first user choice
    if encrypt_or_decrypt == 'e' or encrypt_or_decrypt == 'd':
        message = input('Enter your message now')
        function_to_run = operations[encrypt_or_decrypt]
        print(function_to_run(message))

# Executes the main function
if __name__ == '__main__':
    main()