#Aluguel de carros
day = float(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
custo = float( (day * 60) + (km*0.15) )
print("O total a pagar {:.2f}" .format(custo))