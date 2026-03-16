nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

media = (nota_1+nota_2)/2

if media < 6:
    print("Reprovado!")
elif media >= 6:
    print("Aprovado!")
