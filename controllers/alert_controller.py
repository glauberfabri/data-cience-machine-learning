"""
Gerencia os alertas de preços.
"""
class AlertController:
    """Verifica se os critérios de alerta foram atendidos."""
    @staticmethod
    def check_alert(price: float, alert):
        """
        :param price: Preço atual da criptomoeda.
        :param alert: Objeto da classe Alert.
        """
        if alert.direction == "above" and price > alert.target_price:
            print(f"ALERTA: {alert.symbol} subiu acima de {alert.target_price} USD. Preço atual: {price} USD")
        elif alert.direction == "below" and price < alert.target_price:
            print(f"ALERTA: {alert.symbol} caiu abaixo de {alert.target_price} USD. Preço atual: {price} USD")