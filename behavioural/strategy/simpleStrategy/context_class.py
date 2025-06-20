# context class “Mediator + Wrapper”  ka role karta hai, client isiko call kar rha hai

from strategy_interface import Strategy

class Context:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy         #  Strategy instance ko hold karta hai

    def set_strategy(self, strategy: Strategy):
        self.strategy = strategy        #  Runtime pe switch allow karta hai

    def execute_strategy(self, a, b):
        self.strategy.operations(a, b)  # Delegation / single entry‑point







    
        

