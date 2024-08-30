
#2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(n):
  # algorítmo de fibonacci
  if n > 1:
    return fibonacci(n - 1) + fibonacci(n - 2)
  return n 

def validar_fibonacci(n):
  # inicializador  das variáveis
  count = 0
  fibo = 0

  # repetição while enquanto o valor de fibonnaci for menor ou igual a n
  while fibo <= n:
    fibo = fibonacci(count)

    # condição para verificar se o número pertence a sequência
    if fibo == n:
      return "O número pertence a sequência"
    count += 1

  # caso o número não passe na condição anterior, ele não pertence a sequência
  return "O número não pertence a sequência"

# entrada do usuário para informar o número
num = int(input("Informe um número: "))

print(validar_fibonacci(num))