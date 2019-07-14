#!/usr/bin/python3
# geektechstuff
# Log File Reader

# uses tkinter to draw file dialog screen
from tkinter import *
from tkinter import filedialog

# Colorama allows different colours in terminal
from colorama import init, Fore, Back, Style
init()

# regular expressions for word search
import re

# creates Tk window, hides it and asks the user which file they want to open
def file_browse():
    root = Tk()
    root.withdraw()
    root.update()
    try:
        file_to_open = filedialog.askopenfilename()
    except:
        print("Unable to display File Dialog Window")
    root.destroy()
    return(file_to_open)

# regular expression to search for word in line (case insensitive)
def find_word(word, text):
    search_w = r'(^|[^\w]){}([^\w]|$)'.format(word)
    search_w = re.compile(search_w, re.IGNORECASE)
    search_result = re.search(search_w, text)    
    return bool(search_result)

def log_reader():
    # lists to hold lines depending on content
    error_lines = []
    warning_lines = []
    general_lines = []

    # opens and reads file
    with open(file_browse(), 'r') as filehandle:
        filecontents = filehandle.readlines()
        # ERROR Lines
        for line in filecontents:
            if find_word("error",line) == True:
                print(Fore.RED+line)
                print(Style.RESET_ALL)
            elif find_word("failed",line) == True:
                print(Fore.YELLOW+line)
                print(Style.RESET_ALL)
            else:
                print(Fore.BLUE+line)
                print(Style.RESET_ALL)
    return()
    
log_reader()


