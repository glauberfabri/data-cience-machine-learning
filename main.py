"""
Ponto de entrada do monitor de preços de criptomoedas.
"""
from views.user_view import UserView

if __name__ == "__main__":
    print("Monitor de Preços de Criptomoedas")
    user_view = UserView()

    while True:
        print("\nMenu:")
        print("1. Adicionar alerta")
        print("2. Iniciar monitoramento")
        print("3. Sair")

        choice = input("Escolha uma opção: ")
        if choice == "1":
            user_view.add_alert()
        elif choice == "2":
            user_view.start_monitoring()
        elif choice == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")