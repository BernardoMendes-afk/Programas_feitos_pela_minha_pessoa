semestre = 1

while semestre <= 2:
    print(f"--- NOTAS DO {semestre}º SEMESTRE ---")

    cp1 = float(input("Insira a nota do Checkpoint 1: "))
    cp2 = float(input("Insira a nota do Checkpoint 2: "))
    cp3 = float(input("Insira a nota do Checkpoint 3: "))
    spr1 = float(input("Insira a nota da Sprint 1: "))
    spr2 = float(input("Insira a nota da Sprint 2: "))
    gs = float(input("Insira a nota da Global Solution: "))

    if cp1 <= cp2 and cp1 <= cp3:
        menor_cp = cp1
    elif cp2 <= cp1 and cp2 <= cp3:
        menor_cp = cp2
    else:
        menor_cp = cp3

    media = ((cp1 + cp2 + cp3 - menor_cp + spr1 + spr2) / 4) * 0.4 + (gs * 0.6)

    print("-" * 45)
    print(f"A média do {semestre}º semestre: {media:.1f}")
    print("-" * 45)

    semestre += 1

print("Processamento encerrado.")
