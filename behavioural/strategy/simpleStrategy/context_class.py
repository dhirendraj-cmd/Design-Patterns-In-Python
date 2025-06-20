# context class “Mediator + Wrapper”  ka role karta hai, client isiko call kar rha hai

from strategy_interface import Strategy
from strategy_concrete import AddStrategy, MultiplyStrategy, SubstractStrategy, DivideStrategy

class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy         #  Strategy instance ko hold karta hai

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy        #  Runtime pe switch allow karta hai

    def execute_strategy(self, a, b):
        return self.strategy.operations(a, b)  # Delegation / single entry‑point


# client calling
add = Context(AddStrategy())
print("Adding.... ", add.execute_strategy(5, 7))

subs = Context(SubstractStrategy())
print("Adding.... ", subs.execute_strategy(5, 7))

mul = Context(MultiplyStrategy())
print("Adding.... ", mul.execute_strategy(5, 7))

div = Context(DivideStrategy())
print("Adding.... ", div.execute_strategy(5, 7))






    
        

