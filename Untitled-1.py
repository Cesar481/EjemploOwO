def mostrar_menu():
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Saludar")
    print("2. Calcular sumatoria")
    print("3. Configuración")
    print("4. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-4): ")
        
        match opcion:
            case "1":
                print("\n¡Hola! Espero que estés teniendo un gran día.")
            case "2":
                print("\nFunción para calcular activada.")
                # Aquí puedes agregar tu lógica matemática
            case "3":
                print("\nAbriendo el panel de configuración...")
            case "4":
                print("\n¡Gracias por usar el programa! Saliendo...")
                break
            case _:
                print("\nOpción no válida. Por favor, introduce un número del 1 al 4.")

# Iniciar el programa
if __name__ == "__main__":
    ejecutar_menu()
