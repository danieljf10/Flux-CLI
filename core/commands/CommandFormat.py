class CommandFormat:
    name = ""
    description = ""
    usage = ""

    def run(self, args):
        raise NotImplementedError
    
    def print_usage(self):
        print(f"{self.usage}")

    def parse_flags(self, args):
        flags = {}
        values = []
        for arg in args:
            if arg.startswith("--"):
                flags[arg[2:]] = True ## set string to true
        
            elif arg.startswith("-"):
                for ch in arg[1:]: ## set char to true
                    flags[ch] = True
            else:
                values.append(arg)
        return flags, values
