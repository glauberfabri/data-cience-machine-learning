"""
Gerencia a comunicação com a API de preços.
"""
import requests

class APIController:
    """Gerencia a comunicação com a API pública de criptomoedas."""
    BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

    @staticmethod
    def get_price(symbol: str):
        """Obtém o preço atual de uma criptomoeda."""
        try:
            response = requests.get(f"{APIController.BASE_URL}?ids={symbol}&vs_currencies=usd")
            response.raise_for_status()
            data = response.json()
            return data[symbol]["usd"]
        except Exception as e:
            print(f"Erro ao buscar dados da API: {e}")
            return None
