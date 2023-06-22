# Laço(loop) infinito #
cont = 1
while True:
    print(cont, ' ', end='')
    cont += 1
print('Acabou')

# para ler até uma certa quantidade de números #
n = cont = 0
while cont < 3:  # No exemplo lerá 3 números
    n = int(input('Digite um número: '))
    cont += 1

# Exemplo de como utilizamos o break para interromper loops infinitos #
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))

# Exemplos nova formatação #
nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
