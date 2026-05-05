salario = float(input("Indique seu salário:"))

if salario <= 1250:
    aumento = (salario/100)*15
    print("O aumento será de R$", aumento)

elif salario > 1250:
    aumento = (salario/100)*10
    print("O aumento será de R$", aumento)
