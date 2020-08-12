numerointeiro = int(input("digite um numero inteiro entre 1 e 5: "))
if numerointeiro < 1:
    print("numero invalido!")
elif numerointeiro > 5:
    print("numero invalido!")
else:
    if numerointeiro == 1:
        print("UM")
    elif numerointeiro == 2:
        print("DOIS")
    elif numerointeiro == 3:
        print("TRES")
    elif numerointeiro == 4:
        print("QUATRO")
    else:
        print("CINCO")
