with open('texto.txt', 'w') as arquivo:
    texto = list()
    texto.append("Esta é a primeira frase.")
    texto.append("Aqui está a segunda frase.")
    texto.append("Finalmente, esta é a terceira frase.")
    
    for linha in texto:
        arquivo.write(linha + '\n') 