convert_dict = {
    'A': '.-', 'B': '-...',

    'C': '-.-.', 'D': '-..', 'E': '.',

    'F': '..-.', 'G': '--.', 'H': '....',

    'I': '..', 'J': '.---', 'K': '-.-',

    'L': '.-..', 'M': '--', 'N': '-.',

    'O': '---', 'P': '.--.', 'Q': '--.-',

    'R': '.-.', 'S': '...', 'T': '-',

    'U': '..-', 'V': '...-', 'W': '.--',

    'X': '-..-', 'Y': '-.--', 'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--',

    '4': '....-', '5': '.....', '6': '-....',

    '7': '--...', '8': '---..', '9': '----.',

    '0': '-----', ', ': '--..--', '.': '.-.-.-',

    '?': '..--..', '/': '-..-.', '-': '-....-',

    '(': '-.--.', ')': '-.--.-', ' ': ' ', '  ': ''
}


def encode_string():
    text_to_convert = input('Enter a string that you want to convert: ')
    upper_string = text_to_convert.upper()
    converted = [convert_dict[item] for item in upper_string]
    final_string = ''
    for item in converted:
        final_string += item + ' '
    return final_string


def decode_string():
    inv_dict = {v: k for k, v in convert_dict.items()}
    while True:
        text_to_decode = input("Enter a string in morse variant"
                               " - only '-' and '.' combinations. You need to split"
                               "the symbols by space, and space between words is equal 2")
        try:
            internal_result = text_to_decode.split(' ')
            converted = [inv_dict[item] for item in internal_result]
        except:
            print('Invalid format. Try again!')
            continue
        else:
            final_string = ''
            for item in converted:
                final_string += item
            return final_string.lower().capitalize()


if __name__ == '__main__':
    choice = input('Choose your option: \nEncode: enter 1\nDecode: enter 2\n')
    if choice == '1':
        print(encode_string())
    elif choice == '2':
        print(decode_string())
    else:
        print('Choice a valid option')
