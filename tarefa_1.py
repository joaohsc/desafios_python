#1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

#Resposta: SOMA = 91

# Para responder essa pergunta vou implementar um código exemplo

# declaração das variáveis
id = 13
sum = 0
k=0

# Repetição while com condição de parada quando k < id
while k < id:
  # incremento de k a cada iteração
  k += 1

  # soma da variável sum com o valor de k
  sum = sum+k

print(sum)

