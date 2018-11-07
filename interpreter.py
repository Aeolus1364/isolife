class Interpreter:
    def __init__(self):
        self.priority = 0  # current priority level
        self.current = 0  # current packet

        self.stream = []
        self.var = []
        self.cmds = []  # highest priority command receives arguments

        self.halt = False

    def load(self, stream, var):
        self.stream = stream
        self.var = var

    def step(self):
        packet = self.stream[self.current]
        packtype = self.get_type(packet)
        if self.priority:
            active = self.cmds[self.priority - 1]
        else:
            active = None

        if packtype == "cmd":
            self.priority += 1
            self.cmds.append(self.get_cmd(packet)(self.priority))  # adds new active command
            active = self.cmds[self.priority - 1]

        elif packtype == "val":
            active.argument(packet)  # sends argument to priority command

        if active.complete():  # on command completion
            self.var = active.evaluate(self.var)  # execute command
            del self.cmds[self.priority - 1]  # remove command from active
            self.priority -= 1  # drop priority

        self.current += 1

        print(self.var)

    def get_type(self, packet):  # evaluates whether a packet is a command or value
        if type(packet) == str:
            return "cmd"
        elif type(packet) == int:
            return "val"

    def get_cmd(self, packet):
        if packet == "def":
            return Define
        else:
            self.raise_error(f"{packet} is an invalid command")

    def raise_error(self, error):
        print(error)
        self.halt = True


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


class Define(Command):
    def __init__(self, priority):
        super().__init__(2, priority, "vars")

    def evaluate(self, vars):
        print(self.args)
        vars[self.args[0]] = self.args[1]
        return vars

# class Print(Command):
#     def __init__(self, priority):
#         super().__init__(1, priority)


stream = ['def', 0, 1]
var = []

interpreter = Interpreter()
interpreter.load(stream, var)

for i in stream:
    interpreter.step()