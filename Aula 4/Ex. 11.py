produto = int(input("Indique o indigo do produto: "))
quantidade = int(input("Indique a quantidade desse produto a ser comprada: "))
if produto == 0:
    print("Código inválido")

 while produto != 0:
  if produto == 1:
      preco = produto * 0,5
      quantidade = quantidade + 1
      int(input("Indique o indigo do produto: "))
      int(input("Indique a quantidade desse produto a ser comprada: "))

  elif produto == 2:
      preco = produto
      quantidade = quantidade + 1
      int(input("Indique o indigo do produto: "))
      int(input("Indique a quantidade desse produto a ser comprada: "))

  elif produto == 3:
      preco = produto
      quantidade = quantidade + 4
      int(input("Indique o indigo do produto: "))
      int(input("Indique a quantidade desse produto a ser comprada: "))

  elif produto == 5:
      preco = produto
      quantidade = quantidade + 7
      int(input("Indique o indigo do produto: "))
      int(input("Indique a quantidade desse produto a ser comprada: "))

  elif produto == 9:
      preco = produto
      quantidade = quantidade + 8
      int(input("Indique o indigo do produto: "))
      int(input("Indique a quantidade desse produto a ser comprada: "))

  elif produto == 0:

     break



