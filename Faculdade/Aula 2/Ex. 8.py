m = float(input("Indique o valor da mercadoria: "))
d = float(input("Indique o valor do desconto: "))
print(f"O desconto é de {(m/100)*d} e o preço a pagar é de {m-(m/100)*d}")