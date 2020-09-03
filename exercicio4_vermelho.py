def main():
    valorproduto = float(input("digite o valor do produto: "))
    valordesconto = int(input("digite a porcentagem do desconto: "))
    valordescontado = (valordesconto * valorproduto) / 100
    print("R$:", valorproduto - valordescontado)
    valorpago = float(input("digite o valor pago: "))

    if valorpago < valorproduto - valordescontado:
        print("pague direito!!!")
    else:
        print("compra concluida!!!")
    return print("o troco é de: R$", valorpago - (valorproduto - valordescontado))


main()
