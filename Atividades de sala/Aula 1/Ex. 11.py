#Carro alugado

distancia = float(input("Qual a distância percorrida, em km? :"))
dias = float(input("Por quantos dias o veículo foi alugado? :"))

preco = dias*60+distancia*0.15

print(f"O preço a pagar é: {preco:.2f}.")