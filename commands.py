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
        if self.num_args < 0:
            print("Error: number of arguments less than zero")
        return self.num_args == 0


class Set(Command):  # sets variable value in var stream
    def __init__(self, priority):
        super().__init__(2, priority, "var")
        # arg 0: var name
        # arg 1: var value

    def evaluate(self, var):
        var[self.args[0]] = self.args[1]
        return var


class Get(Command):  # gets variable value from var stream
    def __init__(self, priority):
        super().__init__(1, priority, "value")
        # arg 0: var name

    def evaluate(self,  var):
        return var[self.args[0]]  # returns arg value from var dict


class Print(Command):
    def __init__(self, priority):
        super().__init__(1, priority, "none")
        # arg 0: prints value

    def evaluate(self):
        print(self.args[0])


class Default(Command):
    def __init__(self, priority):
        super().__init__(0, priority, "")

    def evaluate(self):
        pass