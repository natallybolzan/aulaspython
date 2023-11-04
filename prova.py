armazenaidadecachorro = []
armazenaidadegato = []
armazenaidadecoelho = []
femininopreferecachorro = 0
femininopreferegato = 0
femininopreferecoelho = 0
masculinopreferecachorro = 0
masculinopreferegato = 0
masculinopreferecoelho = 0
quantidade = 1
cachorro = 0
gato = 0 
coelho = 0


while True:
    print("Qual animal você prefere:\n")

    animal = int(input("1- Cachorro, 2- Gato, 3- Coelho:\n"))
    idade = int(input("Digite sua idade:\n"))
    print("Digite seu sexo:\n")
    sexo = int(input("1- Feminino, 2- Masculino:\n"))
    print("Deseja continuar?:\n")
    continuar = int(input("1- Sim, 2- Não:\n "))

    if animal == 1:
        armazenaidadecachorro.append(idade)

    if animal == 2:
        armazenaidadegato.append(idade)
    
    if animal == 3:
        armazenaidadecoelho.append(idade)


    if sexo == 1 and animal == 1:
        femininopreferecachorro += 1

    if sexo == 1 and animal == 2:
        femininopreferegato += 1

    if sexo == 1 and animal == 3:
        femininopreferecoelho += 1


    if sexo == 2 and animal == 1:
        masculinopreferecachorro += 1

    if sexo == 2 and animal == 2:
        masculinopreferegato += 1

    if sexo == 2 and animal == 3:
        masculinopreferecoelho += 1

    if animal == 1:
        cachorro += 1

    if animal == 2:
        gato += 1
    
    if animal == 3:
        coelho += 1

    if continuar == 1:
        quantidade += 1

    if continuar == 2:
        break

if len(armazenaidadecachorro) > 0:
    idademaiscachorro = max(
        (armazenaidadecachorro)   
    )
else:
    idademaiscachorro = 0

if len(armazenaidadecachorro) > 0:
    idademenoscachorro = min(
        (armazenaidadecachorro)   
    )
else:
    idademenoscachorro = 0

if len(armazenaidadegato) > 0:
    idademaisgato = max(
        (armazenaidadegato)   
    )
else:
    idademaisgato = 0

if len(armazenaidadegato) > 0:
    idademenosgato = min(
        (armazenaidadegato)   
    )
else:
    idademenosgato = 0

if len(armazenaidadecoelho) > 0:
    idademaiscoelho = max(
        (armazenaidadecoelho)   
    )
else:
    idademaiscoelho = 0

if len(armazenaidadecoelho) > 0:
    idademenoscoelho = min(
        (armazenaidadecoelho)   
    )
else:
    idademenoscoelho = 0
 

porcentagemcachorro = (cachorro / quantidade)*100
porcentagemgato = (gato / quantidade)*100
porcentagemcoelho = (coelho/quantidade)*100

print(f"O total de respondentes foi: {quantidade}\n")

print(f"Porcentagem de pessoas que preferem cachorro: {porcentagemcachorro}%\n")
print(f"Porcentagem de pessoas que preferem gato: {porcentagemgato}%\n")
print(f"Porcentagem de pessoas que preferem coelho: {porcentagemcoelho}%\n")


print(f"A idade da pessoa mais nova que prefere Cachorro é: {idademenoscachorro}\n")
print(f"A idade de pessoa mais velha que prefere Cachorro é: {idademaiscachorro}\n")

print(f"A idade da pessoa mais nova que prefere gato é: {idademenosgato}\n")
print(f"A idade da pessoa mais velha que prefere gato é: {idademaisgato}\n")

print(f"A idade da pessoa mais nova que prefere coelho é: {idademenoscoelho}\n")
print(f"A idade da pessoa mais velha que prefere coelho é: {idademaiscoelho}\n")

print(f"Quantidade de mulheres que preferem cachorro: {femininopreferecachorro}\n")
print(f"Quantidade de mulheres que preferem gato: {femininopreferegato}\n")
print(f"Quantidade de mulheres que preferem coelho: {femininopreferecoelho}\n")

print(f"Quantidade de homens que preferem cachorro: {masculinopreferecachorro}\n")
print(f"Quantidade de homens que preferem gato: {masculinopreferegato}\n")
print(f"Quantidade de homens que preferem coelho {masculinopreferecoelho}\n")
