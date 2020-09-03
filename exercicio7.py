resposta = "s"
soma = quantidade = media = maior = menor = 0
while resposta in "Ss":
    numero = int(input("digite um numero: "))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input("quer continuar? [S/N] ")).upper().strip()[0]

media = soma / quantidade

print("voce digitou {} numeros e a media foi {}".format(quantidade, media))
print("o maior valor foi {} e o menor foi {}".format(maior, menor))
print("Encerrando...")
