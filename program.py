soma = 0
qtd = 0 
while(True):
    entrada = float(input('Entre com um número: ')) # float converte o número para inteiro
    if(entrada == 0):
        break
    soma += entrada # acumulador
    qtd += 1 # contador
media = soma / qtd
print('Soma: ', soma)
print('Quantidade: ', qtd)
print('Média: ', media)