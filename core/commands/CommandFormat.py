class CommandFormat:
    name = ""
    description = ""
    usage = ""

    def run(self, args):
        raise NotImplementedError
    
    def print_usage(self):
        print(f"{self.usage}")
