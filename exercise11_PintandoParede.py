#tinta para parede
a = float(input("Largura da parede: "))
b = float(input("Altura da parede: "))
area = float(a*b)
tinta= float(area/2)
print("Sua parede te a dimensão de {}x{} e sua area é de {:.2f}m². Para pintar essa parede, você precisará de {:.2f} de tinta. " .format(a,b,area,tinta))