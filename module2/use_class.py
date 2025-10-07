class MyClass():
    """
    Demonstrating how classes work.
    """

    def __init__(self, arg1: int, arg2: int):
        self.myfirstarg = arg1
        self.arg2 = arg2
        self.dataid = f"{arg1}_{arg2}"

        self.add_stuff()

    def add_stuff(self):
        print("TEST")
        self.summed_nums = self.myfirstarg + self.arg2

    def increase_arg(self):
        self.add_stuff()
        self.arg2 += 2

    def __str__(self):
        return f"This instance started with {self.myfirstarg} and {self.arg2}"


myinstance = MyClass(2, 5)
print(myinstance.arg2)
for i in range(10):
    myinstance.increase_arg()
print(myinstance.arg2)
print(myinstance)
