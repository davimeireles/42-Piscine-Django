class HotBeverage:
    # Represents a generic hot beverage.
    # This class serves as a base for more specific hot beverage types.
    # It includes a name, price, and a description.
    def __init__(self, name="hot beverage", price=0.30, description="Just some hot water in a cup."):
        self._name = name
        self._price = price
        self._description = description

    def description(self):
        return self._description

    def __str__(self):
        # A formatted string containing the name, price (formatted to two decimal places), and description.
        return f'name: {self._name}\nprice: {self._price:.2f}\ndescription: {self.description()}\n'

class Coffe(HotBeverage):
    # Represents a cup of coffee.
    # Inherits from HotBeverage.
    def __init__(self):
        super().__init__("coffe", 0.40)
        self._description = "A coffee, to stay awake."

class Tea(HotBeverage):
    # Represents a cup of tea.
    # Inherits from HotBeverage.
    def __init__(self):
        super().__init__("tea", 0.30)
        self._description = "Just some hot water in a cup."

class Chocolate(HotBeverage):
    # Represents a cup of chocolate.
    # Inherits from HotBeverage.
    def __init__(self):
        super().__init__("chocolate", 0.50)
        self._description = "Chocolate, sweet chocolate..."

class Capuccino(HotBeverage):
    # Represents a cup of capuccino.
    # Inherits from HotBeverage.
    def __init__(self):
        super().__init__("capuccino", 0.45)
        self._description = "Un po’ di Italia nella sua tazza!"