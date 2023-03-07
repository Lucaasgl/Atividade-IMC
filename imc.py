#Calculadora IMC
peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / altura ** 2

print("Seu IMC é:", imc)


#Maior Valor

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print("O maior valor é:", valor1)
else:
    print("O maior valor é:", valor2)