try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Infelizmente tivemos um problema :(')
    print(f'O problema encontrado foi {erro.__class__}')
except (ValueError, TypeError):
    print('Tivemos um probrlema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados!')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')
