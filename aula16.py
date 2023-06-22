lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# Índices da tupla #
#               0          1        2       3
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])  # Fatiamento

#              -4         -3      -2       -1
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[-2])  # Fatiamento

# Para mostrar todos pelo for #
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')
