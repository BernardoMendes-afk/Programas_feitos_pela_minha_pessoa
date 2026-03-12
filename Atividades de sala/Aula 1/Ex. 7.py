#Salário

salario = float(input("Informe seu salário atual:"))
porcentagem = float(input("Digite a porcentagem de aumento"))

aumento = (salario/100)*porcentagem
novo_salario = salario + aumento

print("Você terá um aumento de R$",aumento)
print("O novo salário será de",novo_salario)
