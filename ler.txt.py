arquivo = open('loremipsum.txt', 'r')
conteudo = arquivo.read()

print("Conteúdo do arquivo:")
print(conteudo)

arquivo.seek(0)  
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha.strip())


arquivo.seek(0)  
tres_primeiros_caracteres = arquivo.read(3)
print("\nPrimeiros 3 caracteres do arquivo:")
print(tres_primeiros_caracteres)


with open('loremipsum.txt', 'r') as arquivo_com_with:
    conteudo_com_with = arquivo_com_with.read()

print("\nConteúdo do arquivo com 'with':")
print(conteudo_com_with)