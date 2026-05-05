velocidade = float(input("Indique a sua velocidade: "))

if velocidade > 80:
    multa = (velocidade-80)*5
    print("Você não é o Dominic Toretto")
    print(f"A multa a ser paga é de R${multa}")

elif velocidade <= 80:
    print("Muito bem!")
