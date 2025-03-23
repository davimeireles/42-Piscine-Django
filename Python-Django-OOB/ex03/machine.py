import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Capuccino

class EmptyCup(HotBeverage):
    # Represents an empty cup, inheriting from HotBeverage.
    def __init__(self):
        # Initializes the EmptyCup with a name, price, and description.
        super().__init__("empty cup", 0.90, "An empty cup?! Gimme my money back!")

class CoffeeMachine:
    # Represents a coffee machine that can serve beverages.
    def __init__(self):
        # Initializes the CoffeeMachine with default values.
        # Sets the total number of cups available in the machine.
        self.total_coups_in_machine = 10
        # Sets the probability of serving an empty cup.
        self.random_chance_to_serve_empty_cup = 0.1
        # Indicates whether the machine is broken.
        self.broken = False

    def serve(self, beverage_type):
        # Serves a beverage of the specified type.
        # Prints a message if the machine is broken.
        if self.broken:
            print("Broken Machine, please fix it first.\n")

        if self.total_coups_in_machine == 0:
            # If there are no cups left, mark the machine as broken and raise an exception.
            self.broken = True
            raise BrokenMachineException()

        if random.random() < self.random_chance_to_serve_empty_cup:
            # Randomly serve an empty cup based on the defined probability.
            beverage_to_serve = EmptyCup()
        else:
            # Otherwise, serve the specified beverage type.
            beverage_to_serve = beverage_type

        # Decrement the total number of cups.
        self.total_coups_in_machine -= 1
        # Return the beverage to be served.
        return beverage_to_serve

    def repair(self):
        # Repairs the coffee machine, resetting its state.
        # Sets the machine to not broken.
        self.broken = False
        # Resets the total number of cups.
        self.total_coups_in_machine = 10
        # Prints a message indicating the machine has been repaired.
        print("Machine was repaired and you can serve beverages again.\n")

class BrokenMachineException(Exception):
    # Represents an exception that is raised when the coffee machine is broken.
    def __init__(self, message = 'This coffee machine has to be repaired.'):
        # Initializes the BrokenMachineException with a default message.
        # Sets the exception message.
        self.message = message
        # Calls the constructor of the parent Exception class.
        super().__init__(self.message)

if __name__ == '__main__':

    # Creates a CoffeeMachine instance.
    machine = CoffeeMachine()
    # Serves a coffee using the serve method.
    beverage = machine.serve(Coffee)

    try:
        for _ in range(11):
            # Attempts to serve coffee 11 times.
            beverage = machine.serve(Coffee())

            # Prints the string representation of the served beverage.
            print(beverage.__str__())
    except BrokenMachineException:
        # If a BrokenMachineException occurs, repair the machine and serve other beverages.

        # Repairs the broken machine.
        machine.repair()
        # Serves a chocolate beverage.
        beverage = machine.serve(Chocolate())
        # Prints the string representation of the served beverage.
        print(beverage.__str__())

        # Serves a tea beverage.
        beverage = machine.serve(Tea())
        # Prints the string representation of the served beverage.
        print(beverage.__str__())