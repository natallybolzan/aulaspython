def na(respostaVelho_):
    if respostaVelho_ == 1:
        return "Ótimo"
    if respostaVelho_ == 2:
        return "Regular"
    if respostaVelho_ == 3:
        return "Bom"
    if respostaVelho_ == 4:
        return "Péssimo"

def naa(respostaNovo_):
    if respostaNovo_ == 1:
        return "Ótimo"
    if respostaNovo_ == 2:
        return "Regular"
    if respostaNovo_ == 3:
        return "Bom"
    if respostaNovo_ == 4:
        return "Péssimo"

print("Digite sua avaliação:")
quantidade = 0
otimo = 0
regular = 0
bom = 0
pessimo = 0
idadeVelho = 0
idadeNovo = 1000000000000000000000
respostaVelho = 0
respostaNovo = 0
while True:
    idade = int(input("informe sua idade: "))
    avaliação = int(input("1- Òtimo, 2- Relugular, 3- Bom, 4-Péssimo: "))
    con = int(input("Deseja continuar? 1- Sim, 2- Não: "))
    quantidade += 1
    if avaliação == 1:
        otimo += 1
    if avaliação == 2:
        regular += 1
    if avaliação == 3:
        bom += 1
    if avaliação == 4:
        pessimo += 1
    if idade > idadeVelho:
        idadeVelho = idade
        respostaVelho = avaliação
    if idade < idadeNovo:
        idadeNovo = idade
        respostaNovo = avaliação
    if con == 2:
        break
idozo=na(respostaVelho)
bebe=naa(respostaNovo)
print("Quantidade de cada resposta:")
print(f"Ótimo: {otimo} | Regular: {regular} | Bom: {bom} | Péssimo: {pessimo}")
print("total respondentes", quantidade)
print(f"A idade do mais velho foi:{idadeVelho} sua resposta foi {idozo}")
print(f"A idade do mais velho foi:{idadeNovo} sua resposta foi {bebe}")
