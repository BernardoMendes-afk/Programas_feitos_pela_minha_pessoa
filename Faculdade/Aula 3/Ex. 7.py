kWh = float(input("Indique a quantidade de kWh consumida: "))
tipo_inst = int(input("Indique o tipo de instalção,sendo elas: 1. R(residêncial), 2. C(comercial) ou 3. I(industrial)  "))

if tipo_inst == 1 and kWh <= 500:
    preco = kWh*0.40
    print(f"O preço a ser pago é R${preco}")
elif tipo_inst == 1 and kWh > 500:
    preco = kWh*0.65
    print(f"O preço a ser pago é R${preco}")
elif tipo_inst == 2 and kWh <= 1000:
    preco = kWh*0.55
    print(f"O preço a ser pago é R${preco}")
elif tipo_inst == 2 and kWh > 1000:
    preco = kWh*0.60
    print(f"O preço a ser pago é R${preco}")
elif tipo_inst == 3 and kWh <= 5000:
    preco = kWh*0.55
    print(f"O preço a ser pago é R${preco}")
elif tipo_inst == 1 and kWh > 5000:
    preco = kWh*0.60
    print(f"O preço a ser pago é R${preco}")
else:
    print("Seu animal")
