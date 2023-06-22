dados = {'nome': 'Pedro'}
print(dados['nome'])

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

 # Keys = k = chaves,   Values = v = valores
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
del pessoas['sexo']  # deleta o elemento sexo
pessoas['nome'] = 'Leandro'  # altera o nome
pessoas['peso'] = 98.5  # adciona elemento
for k, v in pessoas.items():
    print(f'{k} = {v}')
