file = 'arquivo.txt'


arquivo_escrita = open(file, "w")
arquivo_escrita.write("Vou vencer")
arquivo_escrita.close()

arquivo_leitura = open(file, "r")
leitura = arquivo_leitura.read()
print(leitura)
arquivo_leitura.close()
# arquivo_binaria = open(file, 'wb')