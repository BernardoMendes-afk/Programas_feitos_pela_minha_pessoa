distancia = float(input("Indique a dstância a ser percorrida:"))

if distancia <= 200:
    preco = distancia*0.5
    print("O valor a ser pago é R$:", preco)
elif distancia > 200:
    preco = distancia*0.45
    print("O valor a ser pago é R$:", preco)
