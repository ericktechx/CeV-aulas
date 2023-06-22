import math
#ceil
#floor
#trunc
#pow
#sqrt
#factorial

from math import sqrt, floor
num = int(input('Digite um número:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

# Biblioteca random
import random
num = random.randint(1, 10)
print(num)

# Biblioteca emoji
import emoji
print(emoji.emojize("Olá, Mundo :sunglasses:", use_aliases=True))
