#Catetos e Hipotenusa

a = float(input("Comprimento do cateto oposto: "))
b = float(input("Comprimento do cateto adjacente: "))
hipo = float((a**2+b**2)**(1/2))
print("A hipotenusa vai medir {:.2f}" .format(hipo))
