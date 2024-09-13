import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def ler_arquivo(nome_arquivo):
    palavras = []
    with open(nome_arquivo, 'r') as file:
        for linha in file:
            palavras.extend(linha.split())  
    return palavras

def main():
    arquivo_txt = "arquivo.txt" 
    palavras = ler_arquivo(arquivo_txt)
    
    palavras_bubble = palavras[:]
    inicio_bubble = time.time()
    bubble_sort(palavras_bubble)
    fim_bubble = time.time()
    print(f"Bubble Sort: {palavras_bubble[:10]}... (Tempo: {fim_bubble - inicio_bubble:.6f} segundos)")

    palavras_selection = palavras[:]
    inicio_selection = time.time()
    selection_sort(palavras_selection)
    fim_selection = time.time()
    print(f"Selection Sort: {palavras_selection[:10]}... (Tempo: {fim_selection - inicio_selection:.6f} segundos)")

    palavras_sort = palavras[:]
    inicio_sort = time.time()
    palavras_sort.sort()
    fim_sort = time.time()
    print(f"Método nativo sort(): {palavras_sort[:10]}... (Tempo: {fim_sort - inicio_sort:.6f} segundos)")

    with open('palavras_ordenadas.txt', 'w') as file:
        file.write(' '.join(palavras_sort))

if __name__ == "__main__":
    main()