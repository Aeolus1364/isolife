class Command:
    def __init__(self, num_args, priority, return_type):
        self.num_args = num_args  # number of arguments it takes
        self.priority = priority  # priority level of a command
        self.args = []  # list of actual arguments of a function
        self.active = True
        self.return_type = return_type

    def argument(self, arg):
        self.args.append(arg)
        self.num_args -= 1

    def complete(self):
        return self.num_args == 0


class Set(Command):
    def __init__(self, priority):
        super().__init__(2, priority, "var")

    def evaluate(self, var):
        var[self.args[0]] = self.args[1]
        return var
