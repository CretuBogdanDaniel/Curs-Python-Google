lista = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
lista_ascendeta = sorted(lista)
lista_descendenta = sorted(lista,reverse=True)
def mul3():
    for i in lista:
        if(i % 3 == 0):
            print(i, end = ", ")

print(lista_descendenta)
print(lista_ascendeta)
print("Multipli lui 3 sunt: ")
print(end = mul3())

