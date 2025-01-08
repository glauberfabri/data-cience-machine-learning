# Monitor de Preços de Criptomoedas

Este é um programa Python que rastreia preços de criptomoedas em tempo real utilizando a API pública do CoinGecko. Ele permite criar alertas para preços específicos e notifica o usuário quando os critérios são atendidos.

---

## Funcionalidades

- **Rastreamento de Preços:** Acompanha preços de criptomoedas em tempo real.
- **Alertas Personalizados:** Notifica quando o preço de uma criptomoeda ultrapassa um limite superior ou inferior.
- **Monitoramento Contínuo:** Verifica os preços em intervalos de tempo configuráveis.

---

## Estrutura do Projeto

```plaintext
monitor-precos-criptomoedas/
├── models/
│   ├── crypto_model.py       # Representa uma criptomoeda
│   ├── alert_model.py        # Representa os alertas de preço
├── controllers/
│   ├── api_controller.py     # Gerencia a comunicação com a API de preços
│   ├── alert_controller.py   # Processa os alertas
├── views/
│   ├── user_view.py          # Interface com o usuário
├── main.py                   # Ponto de entrada
