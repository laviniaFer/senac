valor = int(input('Entre com um número para saber o fatorial:'))  
fatorial = 1  
while (valor > 1):  
  fatorial = fatorial * valor 
  print(fatorial)
  valor = valor - 1  
print('O fatorial é {}.'.format(fatorial))