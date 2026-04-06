soma = 0
quantidade = 0

numero = int(input("Digite um número (ou 0 para sair): "))

while numero != 0:
    soma = soma + numero
    quantidade = quantidade + 1
    numero = int(input("Digite um número (ou 0 para sair): "))

if quantidade > 0:
    media = soma / quantidade
    print("-" * 30)
    print(f"Quantidade de números: {quantidade}")
    print(f"Soma total: {soma}")
    print(f"Média aritmética: {media:.2f}")
else:
    print("Nenhum número além do zero foi digitado.")