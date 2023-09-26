''' num = int(input("Informe um número para saber quais o números pares até ele: "))
i = 1
for i in range (num+1):
 if (i % 2 == 0):
  print (i) '''
  
entrada = int(input("Digite um numero: "))
cont = 1
acum = 0

while cont < entrada:
    if(acum % 2 == 0):
        acum = acum + cont
        cont+=1
        print(acum)
        
ent = int(input("um número: "))
cont = 1

while cont < ent:
    if (acum % 2 == 0):
        cont+=1
        print(acum)