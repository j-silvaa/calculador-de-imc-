nome = input("Digite o nome: ")
altura = float(input("Digite a altura (em metros): "))
peso = float(input("Digite o peso (em kg): "))

imc = peso / (altura ** 2)

print(f"\nResultado para {nome}:")
print(f"Altura: {altura} m")
print(f"Peso: {peso} kg")
print(f"IMC: {imc:.2f}")
