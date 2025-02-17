# ui module

def welcome_message():
    welcome_header = "=================================================="
    welcome_message1 = "Welcome to Ookami's Document Parser"
    print(f'{welcome_header: ^120}')
    print(f"{welcome_message1: ^120}")
    print(f'{welcome_header: ^120}')

def choose_document():
    choose_document_message1 = "- please choose one of the documents below -"
    print(f'{choose_document_message1: ^120}\n')

    # documents
    moby_dick_text = "Moby Dick"

    # options
    print(f'1 - {moby_dick_text}')

    # end of documents chooseing page
    print(f'\n\n\n\n\n\n\n\n\n\n')