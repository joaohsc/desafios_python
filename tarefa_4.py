#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
#• RJ – R$36.678,66
#• MG – R$29.229,88
#• ES – R$27.165,48
#• Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

# função para retornar o percentual
def get_percentual(n,list):
    soma = sum(list)
    return round((n/soma)*100, 2)

# declaração do dict de faturamento por estado
faturamento_dict = {
    "SP" : 67836.43,
    "RJ" : 36678.66,
    "MG" : 29229.88,
    "ES" : 27165.48,
    "Outros" : 19849.53
}

# percentual de farutramento
percentual = { x: get_percentual(y, list(faturamento_dict.values())) 
              for x,y in faturamento_dict.items() }

# imprimir percentual
for x,y in percentual.items():
    print(f"{x} - percentual: {y}%")