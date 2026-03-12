#Produto

produto = float(input("Indique o valor do produto:"))
porcentagem = float(input("Indique o valor do desconto, em porcentagem:"))

desconto = (produto/100)*porcentagem
novo_valor = produto - desconto

print("O desconto é de R$", desconto)
print("O novo valor do produto é de R$", novo_valor)
