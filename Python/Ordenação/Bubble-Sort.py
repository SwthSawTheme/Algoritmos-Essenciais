numeros = [7,42,5,3,1,6,7,9,0,2,4] # Lista de números a ser ordenado
tamanho = len(numeros)

# Loop principal do Bubble Sort
for i in range(tamanho - 1):
    for j in range(tamanho - i - 1):
        if numeros[j] > numeros[j+1]:
            # Troca os elementos de posição
            numeros[j], numeros[j+1] = numeros[j+1], numeros[j]

# Imprime a lista ordenada
print("Lista ordenada: ")
for i in range(tamanho):
    print(numeros[i], end=" ")