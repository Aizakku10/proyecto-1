print ("concecionario Elba Jito")
int(input("Si desea revisar la lista de automoviles presione 1 y enter"))
print ("1.-ferrari")
print ("2.-tesla")
print ("3.-vento")
print ("4.-island")
print ("5.-rainbow dash")
print ("6.-batimobil")
for i in range (1):
    print("")

int(input("escriba el numero del modelo de carro que desea elegir y presione enter"))

for i in range(len(lista)):
    if lista[i] > n:
        print("------- ")
    elif lista[i] < n:
        print("--------")
    else:
        print("especificaciones")