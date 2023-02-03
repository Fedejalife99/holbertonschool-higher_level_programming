#!/ust/bin/python3
def text_indentation(text):
    if not isinstance(text,str):
        raise TypeError("text must be a string")
    for letter in text:
        if letter in [".", "?", ":"]:
            print('\n')
        else:
            print(letter,end='')
    