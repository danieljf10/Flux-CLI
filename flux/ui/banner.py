from colorama import Fore, init
init(autoreset=True)

BANNER = f""" 
     ▄▄▄▄▄▄▄ ▄▄▄      ▄▄▄  ▄▄▄ ▄▄▄   ▄▄▄    ▄▄▄▄▄▄▄ ▄▄▄      ▄▄▄▄▄ 
    ███▀▀▀▀▀ ███      ███  ███ ████▄████   ███▀▀▀▀▀ ███       ███  
    ███▄▄    ███      ███  ███  ▀█████▀    ███      ███       ███  
    ███▀▀    ███      ███▄▄███ ▄███████▄   ███      ███       ███  
    ███      ████████ ▀██████▀ ███▀ ▀███   ▀███████ ████████ ▄███▄ 
    """
AUTHOR = f"    By Daniel Flemming"

def print_start_banner():
    print(f"{Fore.CYAN}{BANNER}")
    print(f"{AUTHOR}\n")