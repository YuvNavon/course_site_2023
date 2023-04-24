MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
              'D': '-..',    'E': '.',      'F': '..-.',
              'G': '--.',    'H': '....',   'I': '..',
              'J': '.---',   'K': '-.-',    'L': '.-..',
              'M': '--',     'N': '-.',     'O': '---',
              'P': '.--.',   'Q': '--.-',   'R': '.-.',
              'S': '...',    'T': '-',      'U': '..-',
              'V': '...-',   'W': '.--',    'X': '-..-',
              'Y': '-.--',   'Z': '--..',

              '0': '-----',  '1': '.----',  '2': '..---',
              '3': '...--',  '4': '....-',  '5': '.....',
              '6': '-....',  '7': '--...',  '8': '---..',
              '9': '----.',

              '.': '.-.-.-', ',': '--..--', ':': '---...',
              "'": '.----.', '-': '-....-',
              }


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert an input text file to an output Morse code file.

    Notes
    -----
    This function assumes the existence of a MORSE_CODE dictionary, containing a
    mapping between English letters and their corresponding Morse code.

    Parameters
    ----------
    input_file : str
        Path to file containing the text file to convert.
    output_file : str
        Name of output file containing the translated Morse code. Please don't change
        it since it's also hard-coded in the tests file.

        
    Write a program that reads a text file (lorem.txt), converts it to Morse code and writes it back to a new file called lorem_morse.txt
    In the new file, each (Morse) word should be in a new line. Don't loop over the string
    Rather, use built-in Python string methods to do the heavy lifting.
    """

    # Read the text file and convert it to Morse code
    with open(input_file, "r") as file:
        text = file.read().upper()
        morse_text = text.translate(str.maketrans(MORSE_CODE)).replace(' ', '\n')

    # Write the Morse code to a new file
    with open(output_file, "w") as file:
        file.write(morse_text)
    
if __name__ == '__main__':
    english_to_morse()
