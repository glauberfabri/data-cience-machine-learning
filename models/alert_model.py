"""
Define a classe para gerenciar alertas de preço.
"""
class Alert:
    """Classe que define os critérios para alertas."""
    def __init__(self, symbol: str, target_price: float, direction: str):
        """
        :param symbol: Símbolo da criptomoeda (ex.: BTC, ETH).
        :param target_price: Preço-alvo para o alerta.
        :param direction: 'above' para quando o preço subir acima do alvo, 'below' para quando cair abaixo.
        """
        self.symbol = symbol
        self.target_price = target_price
        self.direction = direction