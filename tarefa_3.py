#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import json

def get_dict_list(data):
    return list(data.values())

# abrir json
with open('json/faturamento_empresa.json', 'r') as file:
    faturamento = json.load(file)

# tratar os valores zerados do dicionário
dict_cleaned = { x:y for x,y in faturamento.items() if y != 0 }

dict_list = get_dict_list(dict_cleaned)

# coletar o maior valor do dicionário
maior_valor = max(dict_list)
dia_maior = dict_list.index(maior_valor)

# coletar o menor valor do dicionário
menor_valor = min(dict_list)
dia_menor = dict_list.index(menor_valor)

# média dos valores
media = sum(dict_list)/len(dict_cleaned)
dias = 0

# número de dias com faturamento superior a média
for dict in dict_list:
    if dict > media:
        dias+=1


print(f"O dia {dia_maior} foi o maior faturamento: R$ {maior_valor}")
print(f"O dia {dia_menor} foi o menor faturamento: R$ {menor_valor}")
print(f"N° dias com faturamento superior a média: {dias}")


