#Conversor de temperaturas
a = float(input("Informe a temperatura em °C:"))
novatemperatura = float( (a * 1.8) + 32 )
print("A temperatura de {:.2f} °C corresponde a {:.2f} °F! " .format(a,novatemperatura))