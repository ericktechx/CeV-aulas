# Relembrar rapidamente como funciona a estrutura "for"
for c in range(1, 10):
    print(c)
print('FIM!')

# While
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM!')

# Enquanto o valor digitado for maior que 1, o programa continuará
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM!')

# Quantos números digitados foram impares e quanto foram pares
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares'.format(par, impar))
