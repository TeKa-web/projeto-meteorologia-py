soma = 0
mesesEsc = 0
    
for i in range(12):
   
    mes = int (input("Digite o mês do ano: " ))     

    while mes < 1 or mes > 12 :
        print("Mês inválido! ")
        mes = int (input("Digite o mês novamente: "))

    temperatura = float (input("Digite a temperatura máxima: "))

    while temperatura < -60 or temperatura > 50:
        print("Temperatura inválida!")
        temperatura = float(input("Digite novamente: " ))
    if i == 0:
        maiorTemp = temperatura
        mesMaior = mes
        menorTemp = temperatura
        mesMenor = mes
    soma = soma + temperatura
    if temperatura > 33 :
        mesesEsc = mesesEsc + 1
    if temperatura > maiorTemp:
        maiorTemp = temperatura
        mesMaior = mes
    if temperatura < menorTemp :
        menorTemp = temperatura
        mesMenor = mes      
if mesMaior == 1:
    nomeMesMaior = "janeiro"
elif mesMaior == 2:
    nomeMesMaior = "fevereiro"
elif mesMaior == 3:
    nomeMesMaior = "março"
elif mesMaior == 4:
    nomeMesMaior = "abril"
elif mesMaior == 5:
    nomeMesMaior = "maio"
elif mesMaior == 6:
    nomeMesMaior = "junho"
elif mesMaior == 7:
    nomeMesMaior = "julho"
elif mesMaior == 8:
    nomeMesMaior = "agosto"
elif mesMaior == 9:
    nomeMesMaior = "setembro"
elif mesMaior == 10:
    nomeMesMaior = "outubro"
elif mesMaior == 11:
    nomeMesMaior = "novembro"
elif mesMaior == 12:
    nomeMesMaior = "dezembro"


if mesMenor == 1:
    nomeMesMenor = "janeiro"
elif mesMenor == 2:
    nomeMesMenor = "fevereiro"
elif mesMenor == 3:
    nomeMesMenor = "março"
elif mesMenor == 4:
    nomeMesMenor = "abril"
elif mesMenor == 5:
    nomeMesMenor = "maio"
elif mesMenor == 6:
    nomeMesMenor = "junho"
elif mesMenor == 7:
    nomeMesMenor = "julho"
elif mesMenor == 8:
    nomeMesMenor = "agosto"
elif mesMenor == 9:
    nomeMesMenor = "setembro"
elif mesMenor == 10:
    nomeMesMenor = "outubro"
elif mesMenor == 11:
    nomeMesMenor = "novembro"
elif mesMenor == 12:
    nomeMesMenor = "dezembro"
media = soma / 12
print("A temperatura media do ano é: ",media, "°C")
print("A quantidade de meses escaldantes é: ", mesesEsc, " meses")
print("O mês com a maior temperatura é o mês" ,nomeMesMaior, "E a temperatura foi " ,maiorTemp, "°C")
print("O mês com a menor temperatura é o mês" ,nomeMesMenor, "E a temperatura foi " ,menorTemp, "°C")