"""
Gerencia a exibição de dados para o usuário.
"""
from time import sleep
from controllers.api_controller import APIController
from controllers.alert_controller import AlertController
from models.alert_model import Alert

class UserView:
    """Interface com o usuário para monitoramento em tempo real."""
    def __init__(self):
        self.alerts = []

    def add_alert(self):
        """Adiciona um novo alerta baseado na entrada do usuário."""
        symbol = input("Digite o símbolo da criptomoeda (ex.: bitcoin, ethereum): ").lower()
        target_price = float(input("Digite o preço-alvo para o alerta: "))
        direction = input("Digite 'above' para alerta acima do preço ou 'below' para abaixo: ").lower()

        alert = Alert(symbol, target_price, direction)
        self.alerts.append(alert)
        print(f"Alerta configurado para {symbol.upper()} - Preço: {target_price} USD ({direction}).")

    def start_monitoring(self):
        """Inicia o monitoramento em tempo real."""
        print("Iniciando o monitoramento de preços. Pressione Ctrl+C para encerrar.")
        try:
            while True:
                for alert in self.alerts:
                    price = APIController.get_price(alert.symbol)
                    if price is not None:
                        AlertController.check_alert(price, alert)
                sleep(10)  # Intervalo de 10 segundos entre as verificações
        except KeyboardInterrupt:
            print("Monitoramento encerrado.")