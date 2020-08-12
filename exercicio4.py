def main():
    valorproduto = float(input("digite o valor do produto: "))
    valorpago = float(input("digite o valor pago: "))
    if valorpago < valorproduto:
        print("pague direito!!!")
    else:
        print("compra concluida!!!")
    return print("o troco é de: R$", valorpago - valorproduto)


main()
