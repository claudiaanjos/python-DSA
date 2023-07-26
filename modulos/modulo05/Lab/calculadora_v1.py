# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")

print("Olá! Você está na calculadora em Python")
print(""" 
    Essas são nossas opções de funções:
      [1] para adição;
      [2] para subtração;
      [3] para multiplicação;
      [4] para divisão;
      [0] para sair.
""")
      
funcao = int(input("Digite a opção desejada: ")) 

while funcao != 0:

    if funcao < 0 or funcao > 4:
        print("Opção inválida.")
        break
    
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if funcao == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
    elif funcao == 2:
        print(f"{n1} - {n2} = {n1 - n2}")
    elif funcao == 3:
        print(f"{n1} x {n2} = {n1 * n2}")
    elif funcao == 4:
        print(f"{n1} / {n2} = {n1 / n2}")

    funcao = int(input("Digite a opção desejada: "))

print("Agradecemos por participar do teste da calculadora!")
