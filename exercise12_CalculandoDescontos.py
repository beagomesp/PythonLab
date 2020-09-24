#CalculandoDescontos
a = float(input("Qualé o preço do produto? R$"))
desconto= float(a-(a*0.05))
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f} " .format(a,desconto))
