a_pagar = 0
while True:
    codigo = int(input("Código do produto (0 para sair): "))
    preco = 0
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.5
    elif codigo == 2:
        preco = 1
    elif codigo == 3:
        preco = 4
    elif codigo == 5:
        preco = 7
    elif codigo == 9:
        preco = 8
    else:
        print("Código inválido!")
    if preco != 0:
        quantidade = int(input("Quantidade: "))
        a_pagar = a_pagar + (preco * quantidade)
        print(f"Total a pagar R${apagar:.2f}")






