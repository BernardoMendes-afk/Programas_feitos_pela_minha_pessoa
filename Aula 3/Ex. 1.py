velocidade = float(input("Indique a sua velocidade: "))

if velocidade > 80:
    excesso = velocidade-80
    multa = excesso*5
    print("Você não é o Dominic Toretto")
    print("A multa a ser paga é de R$", multa)

elif velocidade <= 80:
    print("Muito bem!")
