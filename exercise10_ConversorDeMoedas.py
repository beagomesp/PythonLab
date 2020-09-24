#conversor de moeda
a = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = float(a/5.45)
print("Com R${} você pode comprar US${:.2f} " .format(a,dolar))
