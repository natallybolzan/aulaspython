print("Pesquisa sobre o elevador.")
print("Digite o elevador que você mais utilizado:")
print("Qual périodo você utiliza o elevador com mais frequência:")
elevadorA = 0
elevadorB = 0
elevadorC = 0
perAm = 0
perAv = 0
perAn = 0
perBm = 0
perBv = 0
perBn = 0
perCm = 0
perCv = 0
perCn = 0
cont=0

for i in range(3):
    elevador = int(input("1- Elevador A, 2- Elevador B, 3- Elevador C. "))

    if elevador == 1:
        elevadorA += 1
        periodoA = input("m- matutino, v- vespertino, n- noturno.")
        if periodoA == "m":
            perAm += 1
        if periodoA == "v":
            perAv += 1
        if periodoA == "n":
            perAn += 1

    if elevador == 2:
        elevadorB += 1
        periodoB = input("m- matutino, v- vespertino, n- noturno.")
        if periodoB == "m":
            perBm += 1
        if periodoB == "v":
            perBv += 1
        if periodoB == "n":
            perBn += 1

    if elevador == 3:
        elevadorC += 1
        periodoC = input("m- matutino, v- vespertino, n- noturno.\n")
        if periodoC == "m":
            perCm += 1
        if periodoC == "v":
            perCv += 1
        if periodoC == "n":
            perCn += 1
    cont
    print("\n")

elevadorMaisBadalado = max(
    (perAm, "A", "Matutino"),
    (perAv, "A", "vespertino"),
    (perAn, "A", "noturno"),
    (perBm, "B", "Matutino"),
    (perBv, "B", "vespertino"),
    (perBn, "B", "noturno"),
    (perCm, "C", "Matutino"),
    (perCv, "C", "vespertino"),
    (perCn, "C", "noturno"),
)

periodoMaisBadalado = max(
    (perAm+perBm+perCm, "Matutino"),
    (perAv+perBv+perCv, "vespertino"),
    (perAn+perBn+perCn, "noturno"))


periodoMenosBadalado = min(
    (perAm+perBm+perCm, "Matutino"),
    (perAv+perBv+perCv, "vespertino"),
    (perAn+perBn+perCn, "noturno"))

print(f"Elevador mais utilizado é {elevadorMaisBadalado[1]} no periodo {elevadorMaisBadalado[2]}.")
print(f"O periodo mais utilizado é {periodoMaisBadalado[1]} o periodo menos utilizado é {periodoMenosBadalado[1]}.")