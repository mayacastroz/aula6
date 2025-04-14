resp="s"
while resp =="s":
    nota1 = int(input("primeira avaliação"))
while nota1 <0 or nota1>10:
    nota1 = int(input("nota inválida, digite novamente"))



nota2 = int(input("segunda avaliação"))
while nota2 <0 or nota2>10:
    nota2 = int(input("nota inválida, digite novamente"))

media = (nota1+nota2)/2
print(media)

novo = (input("deseja realizar um novo cálculo"))

nota1 = int(input("primeira avaliação"))
while nota1 <0 or nota1>10:
    nota1 = int(input("nota inválida, digite novamente"))

nota2 = int(input("segunda avaliação"))
while nota2 <0 or nota2>10:
    nota2 = int(input("nota inválida, digite novamente"))
repetir = input ("deseja repetir o calculo")
