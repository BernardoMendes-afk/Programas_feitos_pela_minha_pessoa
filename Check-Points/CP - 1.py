cp1 = float(input("Insira a nota do primeiro Check Point: "))
cp2 = float(input("Insira a nota do segundo Check Point: "))
cp3 = float(input("Insira a nota do terceiro Check Point: "))
spr1 = float(input("Insira a nota do primeiro sprint: "))
spr2 = float(input("Insira a nota do segundo sprint: "))
gs = float(input("Insira a nota da Global Solution"))

 if cp1 <= cp2 and cp1 <= cp3:
  media = ((cp2 + cp3) + spr1 + spr2)/4 * 0.4 + gs * 0.6
  media_peso = media  * 0.4
  print(f"A sua média desse semestre é {media:.1f}.")
  print(f"A sua média desse semestre, com peso, é {media_peso:.1f}.")

 elif cp2 <= cp1 and cp2 <= cp3:
    media = ((cp1 + cp3) + spr1 + spr2) / 4 * 0.4 + gs * 0.6
    media_peso = media * 0.4
    print(f"A sua média desse semestre é {media:.1f}.")
    print(f"A sua média desse semestre, com peso, é {media_peso:.1f}.")

 elif cp3 <= cp1 and cp3 <= cp2:
   media = ((cp1 + cp2) + spr1 + spr2) / 4 * 0.4 + gs * 0.6
   media_peso = media * 0.4
   print(f"A sua média desse semestre é {media:.1f}.")
   print(f"A sua média desse semestre, com peso, é {media_peso:.1f}.")

 else:
    print("Erro!")