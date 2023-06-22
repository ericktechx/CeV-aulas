num = [2, 5, 9, 11]
num[2] = 3  # alterar o valor da posição 2
num.append(7)  #adciona o elemento
num.sort()  # organiza a lista
num.sort(reverse=True)  # organiza a lista ao inverso
num.insert(2, 0)  # insere o elemento na posição 2
num.pop()  # remove o último elemento
print(num)
print(f'Essa lista tem {len(num)} elementos')
