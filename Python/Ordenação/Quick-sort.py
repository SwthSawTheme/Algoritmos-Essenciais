# teste de criação do algoritmo Quick Sort - Dividir para conquistar

lista = [4, 1, 2, 7, 90, 8, 65, 32]

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]

    maiores = []
    menores = []

    for i in lista[1:]:
        if i <= pivo:
            menores.append(i)
        else:
            maiores.append(i)
    
    return quick_sort(menores) + [pivo] + quick_sort(maiores)

teste = quick_sort(lista)

print(teste)