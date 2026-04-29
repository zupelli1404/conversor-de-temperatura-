#conversor de temperatura

# Funções de conversão de temperatura
def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32  # Fórmula para converter Celsius em Fahrenheit

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9  # Fórmula para converter Fahrenheit em Celsius

# Funções de conversão de distância
def km_para_milhas(km):
    return km * 0.621371  # 1 km = 0.621371 milhas

def milhas_para_km(mi):
    return mi / 0.621371  # 1 milha = 1.609 km

# Funções de conversão de peso
def kg_para_libras(kg):
    return kg * 2.20462  # 1 kg = 2.20462 libras

def libras_para_kg(lb):
    return lb / 2.20462  # 1 libra = 0.453 kg

# Função principal com menu interativo
def menu():
    while True:  # Loop infinito até o usuário escolher sair
        print("\n=== Conversor de Unidades ===")
        print("1 - Temperatura (C ↔ F)")
        print("2 - Distância (km ↔ milhas)")
        print("3 - Peso (kg ↔ libras)")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")  # Usuário escolhe o tipo de conversão

        # Conversão de temperatura
        if opcao == "1":
            valor = float(input("Digite o valor: "))  # Usuário digita o número
            tipo = input("Converter de (C/F)? ").upper()  # Escolhe se é Celsius ou Fahrenheit
            if tipo == "C":
                print(f"{valor} °C = {celsius_para_fahrenheit(valor):.2f} °F")
            elif tipo == "F":
                print(f"{valor} °F = {fahrenheit_para_celsius(valor):.2f} °C")
            else:
                print("Opção inválida! Digite apenas C ou F.")

        # Conversão de distância
        elif opcao == "2":
            valor = float(input("Digite o valor: "))  # Usuário digita o número
            tipo = input("Converter de (KM/MI)? ").upper()  # Escolhe se é km ou milhas
            if tipo == "KM":
                print(f"{valor} km = {km_para_milhas(valor):.2f} milhas")
            elif tipo == "MI":
                print(f"{valor} milhas = {milhas_para_km(valor):.2f} km")
            else:
                print("Opção inválida! Digite apenas KM ou MI.")

        # Conversão de peso
        elif opcao == "3":
            valor = float(input("Digite o valor: "))  # Usuário digita o número
            tipo = input("Converter de (KG/LB)? ").upper()  # Escolhe se é kg ou libras
            if tipo == "KG":
                print(f"{valor} kg = {kg_para_libras(valor):.2f} libras")
            elif tipo == "LB":
                print(f"{valor} libras = {libras_para_kg(valor):.2f} kg")
            else:
                print("Opção inválida! Digite apenas KG ou LB.")

        # Encerrar programa
        elif opcao == "4":
            print("Encerrando o programa...")
            break  # Sai do loop e encerra o programa

        # Caso o usuário digite uma opção inválida
        else:
            print("Opção inválida! Escolha entre 1 e 4.")

# Executa o programa
if __name__ == "__main__":
    menu()
