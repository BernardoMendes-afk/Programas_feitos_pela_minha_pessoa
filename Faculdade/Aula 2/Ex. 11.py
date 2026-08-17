km = float(input("Insira a distância em Km: "))
d = float(input("Insira a quantidade de dias que o carro foi alugado: "))

p = km*0.15 + d*60
print(f"O preço a pagar é de R${p:.2f}")