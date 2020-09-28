#Reajuste Salarial
a = float(input("Qual é o salário do funcionário R$"))
novosalario = float(a+(a*0.15))
print("Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f} " .format(a,novosalario))
