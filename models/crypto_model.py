"""
Define a classe para representar uma criptomoeda.
"""
class Crypto:
    """Classe que representa uma criptomoeda."""
    def __init__(self, symbol: str, name: str):
        self.symbol = symbol
        self.name = name