import os 
import sys
from storage_json import edit_settings, add_to_history, get_history

def help_cmd(args):
    print("Available Commands:\n",", ".join(basic_commands))

def echo_cmd(args):
    print(" ".join(args))

def set_cmd(args):
    edit_settings(args)

def print_history(args):
    hist_list = get_history()
    for i,item in enumerate(hist_list, 1):
        print(f"{i}: {item}")
    

def exit_cmd(args):
    print("Bye bye!")
    sys.exit(0)

basic_commands = {
    "help": help_cmd,
    "say": echo_cmd,
    "set": set_cmd,
    "history": print_history,
    "exit": exit_cmd
}


def parser(input_stream):
    tokens = input_stream.strip().split()
    command = tokens[0]
    args = tokens[1:]

    add_to_history(input_stream)
    if command in basic_commands:
        basic_commands[command](args)
    else:
        print("Command not recognized. Please enter 'help'")

while (1):
    parser(input("You > "))
