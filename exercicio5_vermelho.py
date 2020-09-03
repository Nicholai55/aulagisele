valor = float(
    input("digite um valor para ver se é positivo ou negativo, impar ou par: "))

if valor < 0:
    print("o valor é negativo!")
else:
    print("o valor é positivo!")

print("e")

if (valor % 2) == 0:
    print("par")
else:
    print("impar")
