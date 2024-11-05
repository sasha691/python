class MorseCode:
    
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 
        'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
        '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', 
        '9': '----.', '0': '-----', ' ': '/'
    }

    TEXT_TO_MORSE = {value: key for key, value in MORSE_CODE_DICT.items()}

    @staticmethod
    def encrypt(text: str):
        text = text.upper()
        morse_code = ' '.join(MorseCode.MORSE_CODE_DICT[char] for char in text if char in MorseCode.MORSE_CODE_DICT)
        return morse_code

    @staticmethod
    def decrypt(morse_code: str):
        words = morse_code.split(' / ') 
        decoded_message = []

        for word in words:
            letters = word.split()  
            decoded_word = ''.join(MorseCode.TEXT_TO_MORSE[letter] for letter in letters if letter in MorseCode.TEXT_TO_MORSE)
            decoded_message.append(decoded_word)

        return ' '.join(decoded_message)
    
    @staticmethod
    def is_morse(text: str):
        valid_symbols = ['.', '-', ' ', '/']
        return all(char in valid_symbols for char in text)