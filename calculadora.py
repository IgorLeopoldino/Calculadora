#input para o usuário responder qual tipo de cálculo ele quer fazer
conta = int(input(f"Qual cálculo você quer fazer?\n1-adição\n2-subtração\n3-divisão\n4-multiplicação\n5-resto_divisao\nEscolha um número: "))

#função que determina qual o nome do cálculo
def nome(conta):
  if conta == 1:
    return "adição"
  
  elif conta == 2:
   return "subtração"
  
  elif conta == 3:
   return "divisão"
  
  elif conta == 4:
   return "multiplicação"

  elif conta == 5:
   return "resto da divisão"

nome_calculo = nome(conta)

print(f"Você escolheu o cálculo de: {nome_calculo}!")

#inputs para o usuário colocar quais números ele quer calcular
num1 = float(input("Digite o primeiro número a ser calculado: "))
num2 = float(input("Digite o segundo número a ser calculado: "))

#função para fazer os cálculos que o usuário pediu
def calculo(conta, num1, num2):
  if conta == 1:
   return num1 + num2
  
  elif conta == 2:
   return num1 - num2

  elif conta == 3:
   return num1 / num2 

  elif conta == 4:
   return num1 * num2
  
  elif conta == 5:
   return num1 % num2

resultado = calculo(conta, num1, num2)

#resposta final para o usuário
print(f"O resultado do cálculo de {nome_calculo} entre os números {num1} e {num2} é: {resultado}")
