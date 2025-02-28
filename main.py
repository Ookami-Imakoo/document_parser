# main
import pyinputplus as pyip
from module import helper, ui

def main():
    ui.welcome_message() # loads welcome message and
    ui.choose_document() # document picker

    # request user input saving to {user_document_choice}
    user_document_choice: int = pyip.inputNum("Enter Document Number: ")
    

    # running document logic
    helper.document_logic_tree(user_document_choice)


main()