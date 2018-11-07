class Test:
    def __init__(self):
        self.var = 23
        self.var2 = 4
        self.ob = Changer()

    def run(self):
        self.ob.func()


class Changer:
    def __init__(self):
        self.num = 7

    def func(self):
        return self.mulitiplier()

    def mulitiplier(self):
        self.num = 4

t = Test()
t.run()