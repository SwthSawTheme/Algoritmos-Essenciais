numeros = [1,2,3,4,5,6,7,8,9]
tamanho = len(numeros)

for i in range(tamanho - 1):
    for j in range(tamanho - i - 1):
        print(f"test: {j}")