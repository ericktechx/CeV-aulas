# Análise
frase = 'Curso em Vídeo Python'
print(frase.count('o'))

# Transformação e Análise
print(frase.upper().count('O'))

# Análise
print(len(frase))

frase1 = '   Curso em Vídeo Python   '  # Aumentará o tamanho do len devido aos espaços
print(len(frase1))

print(len(frase1.strip()))  # Remover espaços inuteis da frase

# Transformação
print(frase.replace('Python', 'Android'))  # Mudança de palavra

 # frase = frase.replace('Python', 'Android') '''Para deixar a transformação salva necessario guardar em uma variável'''

# Análise
print('Curso' in frase)  # Para saber se tem a palavra na frase

# Divisão
print(frase.split())  # Dividi a frase, criando uma lista
