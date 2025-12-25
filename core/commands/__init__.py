from .help import Help 
from .exit import Exit 
from .echo import Echo 
from .clear import Clear 
from .flux import Flux
from .history import History
commands = {
        "help": Help(),
        "exit": Exit(),
        "echo": Echo(),
        "clear": Clear(),
        "flux":Flux(),
        "history": History()
} 