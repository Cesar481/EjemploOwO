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
def mostrar_menu():
    print("\n=== MENÚ CALCULADORA ===")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Salir")

def pedir_numeros():
    # Función auxiliar para evitar repetir código al pedir datos
    try:
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        return n1, n2
    except ValueError:
        print("\n❌ Error: Debes ingresar valores numéricos válidos.")
        return None, None

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-3): ")
        
        match opcion:
            case "1":
                print("\n--- SUMAR ---")
                num1, num2 = pedir_numeros()
                if num1 is not None:
                    resultado = num1 + num2
                    print(f"✅ El resultado de {num1} + {num2} es: {resultado}")
            
            case "2":
                print("\n--- RESTAR ---")
                num1, num2 = pedir_numeros()
                if num1 is not None:
                    resultado = num1 - num2
                    print(f"✅ El resultado de {num1} - {num2} es: {resultado}")
            
            case "3":
                print("\n👋 ¡Gracias por usar la calculadora! Saliendo...")
                break
            
            case _:
                print("\n❌ Opción no válida. Por favor, introduce un número del 1 al 3.")
