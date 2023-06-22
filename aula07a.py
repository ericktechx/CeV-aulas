nome = str(input('Qual é o seu nome? '))
print('Prazer em te conhecer!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# Para não quebrar à linha a utiização do end
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d), end='')
print(', divisão inteira {} e potência {}'.format(di, e))
