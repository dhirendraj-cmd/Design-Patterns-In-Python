from strategy_interface import Strategy

class AddStrategy(Strategy):
    def operations(self, a, b):
        return a+b
    
class SubstractStrategy(Strategy):
    def operations(self, a, b):
        return a-b
    

class MultiplyStrategy(Strategy):
    def operations(self, a, b):
        return a*b
    

class DivideStrategy(Strategy):
    def operations(self, a, b):
        return a/b
