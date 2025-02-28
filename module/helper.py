from pathlib import Path
import pyinputplus as pyip

def text_moby_dick():
    moby_dick_path = Path(r'document_parser\documents\moby_dick') # specific path to moby dick
    moby_dick_text = moby_dick_path.read_text('utf-8') # read that path into variable

    # returns the moby dick text as a string
    return moby_dick_text

def document_logic_tree(user_input):
    """ function for determining user selected document """
    # moby dick
    if user_input == '1':
        print(text_moby_dick())
